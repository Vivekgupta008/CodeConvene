import asyncio
import logging
import sys
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Response

from app.api.router import api_router
from app.core.config import settings
from app.core.orchestration.agent_coordinator import AgentCoordinator
from app.core.orchestration.queue_manager import AsyncQueueManager
from app.database.weaviate.client import get_weaviate_client
from integrations.discord.bot import DiscordBot
from integrations.discord.cogs import CodeConveneelCommands

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class CodeConveneAIApplication:
    """
    Manages the application's core components and background tasks.
    """

    def __init__(self):
        """Initializes all services required by the application."""
        self.weaviate_client = None
        self.queue_manager = AsyncQueueManager()
        self.agent_coordinator = AgentCoordinator(self.queue_manager)
        self.discord_bot = DiscordBot(self.queue_manager)
        self.discord_bot.add_cog(CodeConveneelCommands(self.discord_bot, self.queue_manager))

    async def start_background_tasks(self):
        """Starts the Discord bot and queue workers in the background."""
        try:
            logger.info("Starting background tasks (Discord Bot & Queue Manager)...")

            await self.test_weaviate_connection()

            await self.queue_manager.start(num_workers=3)
            asyncio.create_task(
                self.discord_bot.start(settings.discord_bot_token)
            )
            logger.info("Background tasks started successfully!")
        except Exception as e:
            logger.error(f"Error during background task startup: {e}", exc_info=True)
            await self.stop_background_tasks()

    async def test_weaviate_connection(self):
        """Test Weaviate connection during startup."""
        try:
            async with get_weaviate_client() as client:
                is_ready = await client.is_ready()
                if is_ready:
                    logger.info("Weaviate connection successful and ready")
        except Exception as e:
            logger.error(f"Failed to connect to Weaviate: {e}")
            raise

    async def stop_background_tasks(self):
        """Stops all background tasks and connections gracefully."""
        logger.info("Stopping background tasks and closing connections...")

        try:
            if not self.discord_bot.is_closed():
                await self.discord_bot.close()
                logger.info("Discord bot has been closed.")
        except Exception as e:
            logger.error(f"Error closing Discord bot: {e}", exc_info=True)

        try:
            await self.queue_manager.stop()
            logger.info("Queue manager has been stopped.")
        except Exception as e:
            logger.error(f"Error stopping queue manager: {e}", exc_info=True)

        logger.info("All background tasks and connections stopped.")


# --- FASTAPI LIFESPAN AND APP INITIALIZATION ---
# Global application instance
app_instance = CodeConveneAIApplication()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan manager for the FastAPI application. Handles startup and shutdown events.
    """
    app.state.app_instance = app_instance
    await app_instance.start_background_tasks()
    yield
    await app_instance.stop_background_tasks()


api = FastAPI(title="CodeConvene.AI API", version="1.0", lifespan=lifespan)

@api.get("/favicon.ico")
async def favicon():
    """Return empty favicon to prevent 404 logs"""
    return Response(status_code=204)


api.include_router(api_router)


if __name__ == "__main__":
    required_vars = [
        "DISCORD_BOT_TOKEN", "SUPABASE_URL", "SUPABASE_KEY",
        "BACKEND_URL", "GEMINI_API_KEY", "TAVILY_API_KEY", "GITHUB_TOKEN"
    ]
    missing_vars = [var for var in required_vars if not getattr(settings, var.lower(), None)]

    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)

    uvicorn.run(
        "__main__:api",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
