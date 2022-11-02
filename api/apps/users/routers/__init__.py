from fastapi import APIRouter

from api.apps.users.routers.user import router as user_router
from api.apps.users.routers.role import router as roles_router

users_router = APIRouter(
    prefix="/users",
)
users_router.include_router(user_router)
users_router.include_router(roles_router)
