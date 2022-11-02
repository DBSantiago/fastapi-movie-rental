import pytest
from jose import jwt

from api.apps.users.models import UserRoleModel, UserModel
from api.apps.users.schemas import UserResponse, UserRoleResponse
from api.core.business import Business
from api.core.config import Settings
from api.core.security.hasher import Hasher
from api.core.security.tokens.token_schema import Token


@pytest.fixture
def role_admin(client, session):
    admin_role = UserRoleModel(
        role=Business.ADMIN_ROLE,
        permission_level=Business.ADMIN_PERMISSION
    )

    session.add(admin_role)
    session.commit()
    session.refresh(admin_role)

    return UserRoleResponse.from_orm(admin_role)


@pytest.fixture
def role_employee(client, session):
    emp_role = UserRoleModel(
        role=Business.EMPLOYEE_ROLE,
        permission_level=Business.EMPLOYEE_PERMISSION
    )

    session.add(emp_role)
    session.commit()
    session.refresh(emp_role)

    return UserRoleResponse.from_orm(emp_role)


@pytest.fixture
def admin_user(session, role_admin):
    new_admin = UserModel(
        username=Settings.ADMIN_USERNAME,
        email=Settings.ADMIN_EMAIL,
        password=Hasher.hash_password(Settings.ADMIN_PASSWORD),
        role_id=role_admin.id
    )

    session.add(new_admin)
    session.commit()
    session.refresh(new_admin)

    return UserResponse.from_orm(new_admin)


@pytest.fixture
def admin_login(client, admin_user):
    response = client.post("/auth/token",
                           data={"username": admin_user.username,
                                 "password": Settings.ADMIN_PASSWORD})

    login_res = Token(**response.json())
    payload = jwt.decode(login_res.access_token,
                         Settings.SECRET_KEY,
                         algorithms=[Settings.HASH_ALGORITHM])
    username = payload.get("sub")

    assert username == admin_user.username

    return login_res
