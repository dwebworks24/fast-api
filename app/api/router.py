from fastapi import APIRouter

from app.modules.users.router import router as users_router
from app.modules.auth.router import router as auth_router


api_router = APIRouter()

# Include feature routers
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])

