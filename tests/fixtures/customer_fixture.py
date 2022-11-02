import pytest

from api.apps.customers.models import CustomerModel
from api.apps.customers.schemas import CustomerResponse


@pytest.fixture
def customer(client, session):
    customer = CustomerModel(
        name="John",
        last_name="Doe",
        email="johndoe@email.com"
    )

    session.add(customer)
    session.commit()
    session.refresh(customer)

    return CustomerResponse.from_orm(customer)
