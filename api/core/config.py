import os


class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    PORT = int(os.getenv("PORT"))
    DATABASE_URL = os.getenv("DATABASE_URL")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DEBUG = True if os.getenv("DEBUG") == "True" else False
    HASH_ALGORITHM = os.getenv("HASH_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS")
    ALLOW_CREDENTIALS = os.getenv("ALLOW_CREDENTIALS") == "True"
    ALLOW_METHODS = os.getenv("ALLOW_METHODS")
    ALLOW_HEADERS = os.getenv("ALLOW_HEADERS")
    TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


tags_metadata = [
    {
        "name": "Authentication",
        "description": "Manage user login.",
    },
    {
        "name": "users",
        "description": "Operations with api users.",
    },
    {
        "name": "user roles",
        "description": "Manage roles for api users.",
    },
    {
        "name": "customers",
        "description": "Operations with customers.",
    },
    {
        "name": "genders",
        "description": "Manage genders for cast members.",
    },
    {
        "name": "roles",
        "description": "Manage roles for cast members.",
    },
    {
        "name": "members",
        "description": "Manage cast members for films.",
    },
    {
        "name": "film types",
        "description": "Manage types for films.",
    },
    {
        "name": "film categories",
        "description": "Manage categories for films.",
    },
    {
        "name": "films",
        "description": "Operations with films for renting.",
    },
    {
        "name": "seasons",
        "description": "Manage seasons for films of type Series.",
    },
    {
        "name": "episodes",
        "description": "Manage episodes for films' seasons.",
    },
    {
        "name": "orders",
        "description": "Manage orders for the movie renting process.",
    },

]
