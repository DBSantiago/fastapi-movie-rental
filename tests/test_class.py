from http import HTTPStatus

import pytest


class TestClass:
    @pytest.mark.parametrize("endpoint", [
        "/cast/genders",
        "/cast/roles",
        "/cast/members",
        "/films/types",
        "/films/categories",
        "/films",
        "/customers",
        "/orders",
        "/seasons",
        "/episodes",
        "/users",
        "/users/roles",
    ])
    def test_get_all(self, client, admin_login, role_employee,
                     endpoint):
        response = client.get(
            f"{endpoint}/",
            headers={
                'Authorization': f'{admin_login.token_type} '
                                 f'{admin_login.access_token}'}
        )

        data = response.json().get("data")
        assert response.status_code == HTTPStatus.OK.value
        assert type(data) == list
        assert response.json().get("status") == "success"
