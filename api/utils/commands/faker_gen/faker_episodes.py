import random
from typing import Any

from faker import Faker

from api.apps.seasons.models import EpisodeModel, SeasonModel
from api.db.session import SessionLocal
from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerEpisode(FakerBase):
    """Class for generating Episode records on the database."""
    model = EpisodeModel

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        name = fake.sentence()

        number = fake.pyint(min_value=1, max_value=20)

        return {
            "title": name,
            "number": number,
        }

    @classmethod
    def generate_records(cls):
        with SessionLocal() as db:
            all_seasons = db.query(SeasonModel).all()

        for _ in range(cls.records):
            season = random.choice(all_seasons)
            cls.generate_single_record(season=season)
