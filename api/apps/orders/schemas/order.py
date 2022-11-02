from datetime import date
from decimal import Decimal

from pydantic import BaseModel

from api.apps.customers.schemas import CustomerResponse
from api.apps.films.schemas import FilmResponse


class OrderBase(BaseModel):
    return_date: date
    returned: bool


class OrderRequest(OrderBase):
    customer_id: int
    films: list[int]


class OrderResponse(OrderBase):
    id: int
    rent_date: date
    penalty: Decimal
    total: Decimal
    customer: CustomerResponse
    films: list[FilmResponse]

    class Config:
        orm_mode = True
