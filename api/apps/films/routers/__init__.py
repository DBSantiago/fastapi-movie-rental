from fastapi import APIRouter

from api.apps.films.routers.film_type import router as film_types_router
from api.apps.films.routers.film_category import router as film_categories_router
from api.apps.films.routers.film import router as film_router

films_router = APIRouter(prefix="/films")
films_router.include_router(film_types_router)
films_router.include_router(film_categories_router)
films_router.include_router(film_router)
