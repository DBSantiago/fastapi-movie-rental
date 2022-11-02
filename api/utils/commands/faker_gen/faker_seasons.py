import random
from typing import Any

from faker import Faker

from api.apps.films.models import FilmTypeModel, FilmModel
from api.apps.seasons.models import SeasonModel
from api.db.session import SessionLocal
from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerSeason(FakerBase):
    """Class for generating Season records on the database."""
    model = SeasonModel

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        number = fake.pyint(min_value=1, max_value=10)
        return {
            "number": number,
        }

    @classmethod
    def generate_records(cls):
        with SessionLocal() as db:
            series = db.query(FilmTypeModel).filter(
                FilmTypeModel.film_type == "Series"
            ).first()
            all_series = db.query(FilmModel).filter(
                FilmModel.film_type == series
            ).all()

        for _ in range(cls.records):
            series = random.choice(all_series)
            cls.generate_single_record(series=series)
