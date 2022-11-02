from fastapi import APIRouter

from api.apps.cast.routers.gender import router as genders_router
from api.apps.cast.routers.role import router as roles_router
from api.apps.cast.routers.member import router as members_router

cast_router = APIRouter(prefix="/cast")
cast_router.include_router(genders_router)
cast_router.include_router(roles_router)
cast_router.include_router(members_router)
