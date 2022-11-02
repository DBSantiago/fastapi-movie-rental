from datetime import date, timedelta
from http import HTTPStatus

import pytest

from api.core.business import Business

FILMS_URL = "/films/"


class TestFilms:
    @pytest.mark.parametrize("title, stock, days, status", [
        ("Movie", 20, -7, HTTPStatus.CREATED.value),
        ("      ", 20, -7, HTTPStatus.UNPROCESSABLE_ENTITY.value),
        ("Movie", 2, -7, HTTPStatus.BAD_REQUEST.value),
        ("Movie", 2, 7, HTTPStatus.BAD_REQUEST.value),
    ])
    def test_create_film(self, client, session, admin_login,
                         film_type, film_category, cast_member,
                         title, stock, days, status):
        release = date.today() + timedelta(days=days)
        release = release.strftime(Business.DATE_FORMAT)
        response = client.post(
            FILMS_URL,
            json={
                "title": title,
                "description": "A very good test film",
                "price": 25.00,
                "stock": stock,
                "availability": 10,
                "release_date": release,
                "film_type_id": film_type.id,
                "categories": [
                    film_category.id
                ],
                "cast": [
                    cast_member.id
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
