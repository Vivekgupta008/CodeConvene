from fastapi import Request
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import CodeConveneAIApplication

async def get_app_instance(request: Request) -> "CodeConveneAIApplication":
    """
    Dependency to get the application instance from FastAPI's state.
    This avoids circular imports by using dependency injection.
    """
    return request.app.state.app_instance
