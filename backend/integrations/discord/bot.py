import discord
from discord.ext import commands
import logging
from typing import Dict, Any, Optional
from app.core.orchestration.queue_manager import AsyncQueueManager, QueuePriority
from app.agents.classification_router import ClassificationRouter

logger = logging.getLogger(__name__)

class DiscordBot(commands.Bot):
    """Discord bot with LangGraph agent integration"""

    def __init__(self, queue_manager: AsyncQueueManager, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.members = True
        intents.dm_messages = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            **kwargs
        )

        self.queue_manager = queue_manager
        self.classifier = ClassificationRouter()
        self.active_threads: Dict[str, str] = {}  # user_id -> thread_id mapping

        # Register queue handlers
        self._register_queue_handlers()

    def _register_queue_handlers(self):
        """Register handlers for queue messages"""
        self.queue_manager.register_handler("discord_response", self._handle_agent_response)

    async def on_ready(self):
        """Bot ready event"""
        logger.info(f'Enhanced Discord bot logged in as {self.user}')
        print(f'Bot is ready! Logged in as {self.user}')

    async def on_message(self, message):
        """Enhanced message handling with classification"""
        if message.author == self.user:
            return

        # if message is a command (starts with !)
        ctx = await self.get_context(message)
        if ctx.command is not None:
            await self.invoke(ctx)
            return

        try:
            # Classify message locally first
            classification = await self.classifier.classify_message(
                message.content,
                {
                    "channel_id": str(message.channel.id),
                    "user_id": str(message.author.id),
                    "guild_id": str(message.guild.id) if message.guild else None
                }
            )

            logger.info(f"Message classified as: {classification}")

            # Only process if CodeConveneel intervention is needed
            if classification.get("needs_CodeConveneel", False):
                await self._handle_CodeConveneel_message(message, classification)

        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")

    async def _handle_CodeConveneel_message(self, message, classification: Dict[str, Any]):
        """Handle messages that need CodeConveneel intervention"""
        try:
            user_id = str(message.author.id)

            # Get or create thread for this user
            thread_id = await self._get_or_create_thread(message, user_id)

            # Prepare message for agent processing
            agent_message = {
                "type": "CodeConveneel_request",
                "id": f"discord_{message.id}",
                "user_id": user_id,
                "channel_id": str(message.channel.id),
                "thread_id": thread_id,
                "memory_thread_id": user_id,
                "content": message.content,
                "classification": classification,
                "platform": "discord",
                "timestamp": message.created_at.isoformat(),
                "author": {
                    "username": message.author.name,
                    "display_name": message.author.display_name
                }
            }

            # Determine priority based on classification
            priority_map = {
                "high": QueuePriority.HIGH,
                "medium": QueuePriority.MEDIUM,
                "low": QueuePriority.LOW
            }
            priority = priority_map.get(classification.get("priority"), QueuePriority.MEDIUM)

            # Enqueue for agent processing
            await self.queue_manager.enqueue(agent_message, priority)

            # Send acknowledgment in thread
            if thread_id:
                thread = self.get_channel(int(thread_id))
                if thread:
                    await thread.send("I'm processing your request, please hold on...")

        except Exception as e:
            logger.error(f"Error handling CodeConveneel message: {str(e)}")

    async def _get_or_create_thread(self, message, user_id: str) -> Optional[str]:
        """Get existing thread or create new one for user"""
        try:
            # Check if user already has an active thread
            if user_id in self.active_threads:
                thread_id = self.active_threads[user_id]
                thread = self.get_channel(int(thread_id))

                # Verify thread still exists and is active
                if thread and not thread.archived:
                    return thread_id
                else:
                    del self.active_threads[user_id]
                    logger.info(f"Cleaned up archived thread for user {user_id}")

            # Create new thread
            thread_name = f"CodeConveneel Chat - {message.author.display_name}"

            if isinstance(message.channel, discord.TextChannel):
                thread = await message.create_thread(
                    name=thread_name,
                    auto_archive_duration=60  # 1 hour
                )

                # Store thread mapping
                self.active_threads[user_id] = str(thread.id)

                # Send welcome message
                await thread.send(
                    f"Hello {message.author.mention}! 👋\n"
                    f"I'm your CodeConveneel assistant. I can help you with:\n"
                    f"• Technical questions about CodeConvene.AI\n"
                    f"• Getting started and onboarding\n"
                    f"• Searching for information on the web\n"
                    f"• General developer support\n\n"
                    f"This thread keeps our conversation organized!"
                )

                return str(thread.id)

        except Exception as e:
            logger.error(f"Failed to create thread: {str(e)}")

        return str(message.channel.id)  # Fallback to original channel

    async def _handle_agent_response(self, response_data: Dict[str, Any]):
        """Handle response from CodeConveneel agent"""
        try:
            thread_id = response_data.get("thread_id")
            response_text = response_data.get("response", "")

            if not thread_id or not response_text:
                logger.warning("Invalid agent response data")
                return

            thread = self.get_channel(int(thread_id))
            if thread:
                # Split long responses into multiple messages
                if len(response_text) > 2000:
                    chunks = [response_text[i:i+2000] for i in range(0, len(response_text), 2000)]
                    for chunk in chunks:
                        await thread.send(chunk)
                else:
                    await thread.send(response_text)
            else:
                logger.error(f"Thread {thread_id} not found for agent response")

        except Exception as e:
            logger.error(f"Error handling agent response: {str(e)}")
