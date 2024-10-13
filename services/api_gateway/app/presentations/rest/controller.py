# services/api_gateway/app/api/__init__.py
from api_gateway.app.presentations.rest.auth.auth_controller import auth_router
from api_gateway.app.presentations.rest.user.user_controller import user_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])

