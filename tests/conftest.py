import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from api.core.config import Settings
from api.db.base_class import Base
from api.dependencies.db import get_db
from main import app
from tests.fixtures.user_fixtures import (
    admin_login, admin_user, role_admin, role_employee,
)
from tests.fixtures.cast_fixtures import (
    cast_gender, cast_member, cast_role,
)
from tests.fixtures.film_fixtures import (
    film, film_category, film_type,
)
from tests.fixtures.customer_fixture import customer

engine = create_engine(Settings.TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
