import logging
from typing import Dict, Any
from functools import partial
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from ..base_agent import BaseAgent, AgentState
from ..classification_router import MessageCategory
from .tools.search_tool import TavilySearchTool
from .tools.faq_tool import FAQTool
from app.core.config import settings
from .nodes.gather_context import gather_context_node
from .nodes.handlers.faq import handle_faq_node
from .nodes.handlers.web_search import handle_web_search_node
from .nodes.handlers.technical_support import handle_technical_support_node
from .nodes.handlers.onboarding import handle_onboarding_node
from .generate_response_node import generate_response_node
from .nodes.summarization import check_summarization_needed, summarize_conversation_node, store_summary_to_database

logger = logging.getLogger(__name__)

class CodeConveneelAgent(BaseAgent):
    """CodeConveneel LangGraph Agent for community support and engagement"""

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.llm = ChatGoogleGenerativeAI(
            model=settings.CodeConveneel_agent_model,
            temperature=0.3,
            google_api_key=settings.gemini_api_key
        )
        self.search_tool = TavilySearchTool()
        self.faq_tool = FAQTool()
        self.checkpointer = InMemorySaver()
        super().__init__("CodeConveneelAgent", self.config)

    def _build_graph(self):
        """Build the CodeConveneel agent workflow graph"""
        workflow = StateGraph(AgentState)

        # Add nodes
        workflow.add_node("gather_context", gather_context_node)
        workflow.add_node("handle_faq", partial(handle_faq_node, faq_tool=self.faq_tool))
        workflow.add_node("handle_web_search", partial(
            handle_web_search_node, search_tool=self.search_tool, llm=self.llm))
        workflow.add_node("handle_technical_support", handle_technical_support_node)
        workflow.add_node("handle_onboarding", handle_onboarding_node)
        workflow.add_node("generate_response", partial(generate_response_node, llm=self.llm))
        workflow.add_node("check_summarization", check_summarization_needed)
        workflow.add_node("summarize_conversation", partial(summarize_conversation_node, llm=self.llm))

        # Add edges
        workflow.add_conditional_edges(
            "gather_context",
            self._route_to_handler,
            {
                MessageCategory.FAQ: "handle_faq",
                MessageCategory.WEB_SEARCH: "handle_web_search",
                MessageCategory.ONBOARDING: "handle_onboarding",
                MessageCategory.TECHNICAL_SUPPORT: "handle_technical_support",
                MessageCategory.COMMUNITY_ENGAGEMENT: "handle_technical_support",
                MessageCategory.DOCUMENTATION: "handle_technical_support",
                MessageCategory.BUG_REPORT: "handle_technical_support",
                MessageCategory.FEATURE_REQUEST: "handle_technical_support",
                MessageCategory.NOT_CodeConveneEL: "handle_technical_support"
            }
        )

        # All handlers lead to response generation
        for node in ["handle_faq", "handle_web_search", "handle_technical_support", "handle_onboarding"]:
            workflow.add_edge(node, "generate_response")

        workflow.add_edge("generate_response", "check_summarization")

        # Conditional edge for summarization
        workflow.add_conditional_edges(
            "check_summarization",
            self._should_summarize,
            {
                "summarize": "summarize_conversation",
                "end": END
            }
        )

        # End after summarization
        workflow.add_edge("summarize_conversation", END)

        # Set entry point
        workflow.set_entry_point("gather_context")

        # Compile with InMemorySaver checkpointer
        self.graph = workflow.compile(checkpointer=self.checkpointer)

    def _route_to_handler(self, state: AgentState) -> str:
        """Route to the appropriate handler based on intent"""
        classification = state.context.get("classification", {})
        intent = classification.get("category")

        if isinstance(intent, str):
            try:
                intent = MessageCategory(intent.lower())
            except ValueError:
                logger.warning(f"Unknown intent string '{intent}', defaulting to TECHNICAL_SUPPORT")
                intent = MessageCategory.TECHNICAL_SUPPORT

        logger.info(f"Routing based on intent: {intent} for session {state.session_id}")

        # Mapping from MessageCategory enum to string keys used in add_conditional_edges
        if intent in [MessageCategory.FAQ, MessageCategory.WEB_SEARCH,
                      MessageCategory.ONBOARDING, MessageCategory.TECHNICAL_SUPPORT,
                      MessageCategory.COMMUNITY_ENGAGEMENT, MessageCategory.DOCUMENTATION,
                      MessageCategory.BUG_REPORT, MessageCategory.FEATURE_REQUEST,
                      MessageCategory.NOT_CodeConveneEL]:
            logger.info(f"Routing to handler for: {intent}")
            return intent

        # Later to be changed to handle anomalies
        logger.info(f"Unknown intent '{intent}', routing to technical support")
        return MessageCategory.TECHNICAL_SUPPORT

    def _should_summarize(self, state: AgentState) -> str:
        """Determine if conversation should be summarized"""
        if state.summarization_needed:
            logger.info(f"Summarization needed for session {state.session_id}")
            return "summarize"
        return "end"

    async def get_thread_state(self, thread_id: str) -> Dict[str, Any]:
        """Get the current state of a thread"""
        try:
            config = {"configurable": {"thread_id": thread_id}}
            state = self.graph.get_state(config)
            return state.values if state else {}
        except Exception as e:
            logger.error(f"Error getting thread state: {str(e)}")
            return {}

    async def clear_thread_memory(self, thread_id: str, force_clear: bool = False) -> bool:
        """Clear memory for a specific thread using memory_timeout_reached flag"""
        try:
            config = {"configurable": {"thread_id": thread_id}}
            state = self.graph.get_state(config)

            if state and state.values:
                agent_state = AgentState(**state.values)

                # Check the memory_timeout_reached flag
                if agent_state.memory_timeout_reached or force_clear:
                    if agent_state.memory_timeout_reached:
                        logger.info(f"Thread {thread_id} timeout flag set, storing final summary and clearing memory")
                    else:
                        logger.info(f"Force clearing memory for thread {thread_id}")

                    # Store final summary to database before clearing
                    await store_summary_to_database(agent_state)

                    # Delete the thread from InMemorySaver
                    self.checkpointer.delete_thread(thread_id)
                    logger.info(f"Successfully cleared memory for thread {thread_id}")
                    return True
                else:
                    logger.info(f"Thread {thread_id} has not timed out, memory preserved")
                    return False
            else:
                logger.info(f"No state found for thread {thread_id}, nothing to clear")
                return True

        except Exception as e:
            logger.error(f"Error clearing thread memory: {str(e)}")
            return False
