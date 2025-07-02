import logging
from app.agents.state import AgentState

logger = logging.getLogger(__name__)

async def handle_technical_support_node(state: AgentState) -> AgentState:
    """Handle technical support requests"""
    logger.info(f"Handling technical support for session {state.session_id}")

    return {
        "task_result": {
            "type": "technical_support",
            "action": "provide_guidance",
            "requires_human_review": False
        },
        "current_task": "technical_support_handled"
    }
