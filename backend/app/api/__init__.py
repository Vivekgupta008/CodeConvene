"""
API package for the CodeConvene.AI backend.

This package contains all API-related components:
- router: Main API router with all endpoints
- v1: Version 1 API endpoints
"""

from .router import api_router

__all__ = ["api_router"]
