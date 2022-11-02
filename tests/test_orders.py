from datetime import date, timedelta
from http import HTTPStatus

import pytest

from api.core.business import Business

ORDERS_URL = "/orders/"


class TestOrders:
    @pytest.mark.parametrize("days, status", [
        (2, HTTPStatus.CREATED.value),
        (20, HTTPStatus.BAD_REQUEST.value),
        (-3, HTTPStatus.BAD_REQUEST.value)
    ])
    def test_create_order(self, client, admin_login, role_employee,
                          film, customer, days, status):
        return_on = date.today() + timedelta(days=days)
        return_on = return_on.strftime(Business.DATE_FORMAT)
        response = client.post(
            ORDERS_URL,
            json={
                "return_date": return_on,
                "returned": False,
                "customer_id": customer.id,
                "films": [
                    film.id
                ]
            },
            headers={
                'Authorization': f'{admin_login.token_type} '
                                 f'{admin_login.access_token}'}
        )
        data = response.json().get("data")
        assert response.status_code == status
        if status == HTTPStatus.CREATED.value:
            assert data.get("id")
