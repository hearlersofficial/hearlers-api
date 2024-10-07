# services/api_gateway/app/api/__init__.py
from api_gateway.app.presentations.rest.user.user_controller import \
    router as user_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
