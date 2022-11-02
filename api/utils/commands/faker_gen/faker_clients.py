from typing import Any

from faker import Faker

from api.apps.customers.models import CustomerModel
from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerCustomer(FakerBase):
    """Class for generating Customer records on the database."""
    model = CustomerModel

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        full_name = fake.name().split()
        name = full_name[0]
        last_name = full_name[1]
        email = fake.safe_email()

        return {
            "name": name,
            "last_name": last_name,
            "email": email,
        }
