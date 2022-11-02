from datetime import date, timedelta

import pytest

from api.apps.cast.models import MemberModel
from api.apps.films.models import (
    FilmTypeModel, FilmCategoryModel, FilmModel,
)
from api.apps.films.schemas import (
    FilmTypeResponse, FilmCategoryResponse, FilmResponse,
)


@pytest.fixture
def film_type(client, session):
    film_type = FilmTypeModel(
        film_type="Series"
    )

    session.add(film_type)
    session.commit()
    session.refresh(film_type)

    return FilmTypeResponse.from_orm(film_type)


@pytest.fixture
def film_category(client, session):
    film_category = FilmCategoryModel(
        category="Fantasy"
    )

    session.add(film_category)
    session.commit()
    session.refresh(film_category)

    return FilmCategoryResponse.from_orm(film_category)


@pytest.fixture
def film(client, session, film_category, film_type, cast_member):
    category = session.query(FilmCategoryModel).filter(
        FilmCategoryModel.id == film_category.id
    ).first()
    member = session.query(MemberModel).filter(
        MemberModel.id == cast_member.id
    ).first()
    film = FilmModel(
        title="New film",
        description="New test film",
        price=25.00,
        stock=10,
        availability=10,
        release_date=date.today() - timedelta(days=1),
        film_type_id=film_type.id,
        categories=[category],
        cast=[member]
    )

    session.add(film)
    session.commit()
    session.refresh(film)

    return FilmResponse.from_orm(film)
