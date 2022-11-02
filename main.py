from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.apps.cast.routers import cast_router
from api.apps.films.routers import films_router
from api.apps.customers.routers import customers_router
from api.apps.orders.routers import orders_router
from api.apps.seasons.routers import seasons_router, episodes_router
from api.apps.users.routers import users_router
from api.core.config import Settings, tags_metadata
from api.core.security.authentication import login_router

app = FastAPI(
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.ALLOW_ORIGINS,
    allow_credentials=Settings.ALLOW_CREDENTIALS,
    allow_methods=Settings.ALLOW_METHODS,
    allow_headers=Settings.ALLOW_HEADERS,
)

app.include_router(login_router)
app.include_router(cast_router)
app.include_router(films_router)
app.include_router(customers_router)
app.include_router(orders_router)
app.include_router(seasons_router)
app.include_router(episodes_router)
app.include_router(users_router)
