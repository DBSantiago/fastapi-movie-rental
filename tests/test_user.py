from http import HTTPStatus

import pytest

from api.core.config import Settings
from api.core.security.hasher import Hasher

USERS_URL = "/users"


class TestUsers:
    @pytest.mark.parametrize("username, email, password, status_code", [
        ("bestuser", "thebest@email.com",
         "bestuser", HTTPStatus.CREATED.value),
        ("", "newuser@email.com",
         "password", HTTPStatus.UNPROCESSABLE_ENTITY.value),
        ("neweruser", "newuser@email.com",
         "      ", HTTPStatus.UNPROCESSABLE_ENTITY.value),
    ])
    def test_create_user(self, client, admin_login, role_admin,
                         username, email, password, status_code):
        response = client.post(
            f"{USERS_URL}/",
            json={
                "username": username,
                "email": email,
                "password": password,
                "role_id": role_admin.id
            },
            headers={
                'Authorization': f'{admin_login.token_type} '
                                 f'{admin_login.access_token}'}
        )
        data = response.json().get("data")
        assert response.status_code == status_code
        if status_code == HTTPStatus.CREATED.value:
            assert data.get("email") == email

    def test_get_user_by_id(self, client, admin_login, admin_user):
        response = client.get(
            f"{USERS_URL}/{admin_user.id}",
            headers={
                'Authorization': f'{admin_login.token_type} '
                                 f'{admin_login.access_token}'}
        )

        data = response.json().get("data")
        assert response.status_code == HTTPStatus.OK.value
        assert data.get("id") == admin_user.id
        assert data.get("email") == admin_user.email

    @pytest.mark.parametrize("updated_user, updated_email, status", [
        ("newadmin", "newadmin@email.com", HTTPStatus.OK.value),
        ("", "newadmin@email.com",
         HTTPStatus.UNPROCESSABLE_ENTITY.value),
        ("newadmin", "          ",
         HTTPStatus.UNPROCESSABLE_ENTITY.value),
    ])
    def test_update_user(self, client, admin_user, admin_login,
                         updated_user, updated_email, status):
        response = client.put(
            f"{USERS_URL}/{admin_user.id}",
            json={
                "username": updated_user,
                "email": updated_email,
                "password": Hasher.hash_password(Settings.ADMIN_PASSWORD),
                "role_id": admin_user.role.id
            },
            headers={
                'Authorization': f'{admin_login.token_type} '
                                 f'{admin_login.access_token}'}
        )
        data = response.json().get("data")
        assert response.status_code == status
        if response.status_code == HTTPStatus.OK.value:
            assert data.get("email") == updated_email
            assert data.get("id") == admin_user.id
