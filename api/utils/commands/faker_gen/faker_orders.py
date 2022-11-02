import random
from datetime import date, timedelta
from typing import Any

from faker import Faker

from api.apps.customers.models import CustomerModel
from api.apps.films.models import FilmModel
from api.apps.orders.models import OrderModel
from api.db.session import SessionLocal
from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerOrder(FakerBase):
    """Class for generating Order records on the database."""
    model = OrderModel

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        end_date = date.today() + timedelta(days=13)
        # Apparently future_date returns a tuple with
        # a single datetime.date object so we'll access it by index
        return_date = fake.future_date(end_date=end_date),
        returned = random.choice([True, False])

        return {
            "return_date": return_date[0],
            "returned": returned,
        }

    @classmethod
    def generate_records(cls):
        with SessionLocal() as db:
            customers = db.query(CustomerModel).all()
            films = db.query(FilmModel).all()

        for _ in range(cls.records):
            cls.generate_single_record(
                customer=random.choice(customers),
                films=random.sample(films, 2)
            )
