import random
from datetime import date
from decimal import Decimal
from typing import Any

from faker import Faker

from api.apps.cast.models import MemberModel
from api.apps.films.models import FilmModel, FilmTypeModel, FilmCategoryModel
from api.db.session import SessionLocal
from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerFilm(FakerBase):
    """Class for generating Film records on the database."""
    model = FilmModel

    @classmethod
    def generate_film_types(cls):
        with SessionLocal() as db:
            all_types = {film_type.type for film_type
                         in db.query(FilmTypeModel).all()}
            film_types = {"Movie", "Series"}
            for film_type in film_types.difference(all_types):
                obj = FilmTypeModel(film_type=film_type)
                db.add(obj)
                db.commit()
                db.refresh(obj)

    @classmethod
    def generate_film_categories(cls):
        with SessionLocal() as db:
            all_categories = [category.category for category
                              in db.query(FilmCategoryModel).all()]
            categories = {"Action", "Comedy", "Drama", "Fantasy", "Horror",
                          "Mystery", "Romance", "Thriller", "Western"}
            for category in categories.difference(all_categories):
                obj = FilmCategoryModel(category=category)
                db.add(obj)
                db.commit()
                db.refresh(obj)

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        title = fake.sentence()
        description = fake.text()
        price = fake.pydecimal(right_digits=2, left_digits=2,
                               positive=True, min_value=Decimal("0.01"))
        stock = fake.pyint(min_value=20, max_value=40)
        release_date = fake.date(end_datetime=date(2022, 8, 31))

        return {
            "title": title,
            "description": description,
            "price": price,
            "stock": stock,
            "availability": stock,
            "release_date": release_date,
        }

    @classmethod
    def generate_records(cls):
        cls.generate_film_types()
        cls.generate_film_categories()
        with SessionLocal() as db:
            film_types = db.query(FilmTypeModel).all()
            film_categories = db.query(FilmCategoryModel).all()
            cast_members = db.query(MemberModel).all()

        for _ in range(cls.records):
            categories = random.sample(film_categories, 3)
            cast = random.sample(cast_members, 3)
            cls.generate_single_record(
                film_type=random.choice(film_types),
                categories=categories,
                cast=cast
            )
