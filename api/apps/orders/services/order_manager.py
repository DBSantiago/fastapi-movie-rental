from datetime import date
from decimal import Decimal
from typing import Generator, Any

from api.apps.films.models import FilmModel
from api.apps.orders.models import OrderModel
from api.apps.orders.services.order_validator import OrderValidator
from api.apps.orders.schemas import OrderRequest
from api.core.business import Business
from api.db.managers.query_manager import QueryManager


class OrderManager(QueryManager):
    validation_class = OrderValidator

    @staticmethod
    def update_order_film_availability(*, data: dict[str, Any],
                                       db: Generator,
                                       amount: int) -> None:
        """Update the availability of films when rented or returned."""
        for film in data.get("films"):
            film.availability += amount
            db.add(film)
            db.commit()
            db.refresh(film)

    @staticmethod
    def calculate_penalty(*, data: dict[str, Any]) -> Decimal:
        """Calculate an order's penalty when returned."""
        penalty = Decimal("0.00")

        return_date = data.get("return_date")
        date_diff = date.today() - return_date

        if date_diff.days > 0:
            penalty += Business.PENALTY_PER_DAY * date_diff.days
            for film in data.get("films"):
                penalty += film.price * date_diff.days

        return penalty

    @staticmethod
    def calculate_order_price(*, data: dict[str, Any]) -> Decimal:
        """Calculate an order's price based on its films."""
        price = Decimal("0.00")

        rent_date = data.get("rent_date")
        return_date = data.get("return_date")
        rent_days = return_date - rent_date

        for film in data.get("films"):
            price += film.price * rent_days.days

        return price

    @classmethod
    def prepare_data(cls, *, data: OrderRequest, db: Generator):
        """Prepare an order's data before posting or updating."""
        data = data.dict()
        data["rent_date"] = date.today()
        data["films"] = cls.get_nested_model(data=data,
                                             field="films",
                                             model=FilmModel,
                                             db=db)
        data["penalty"] = cls.calculate_penalty(data=data)
        data["total"] = cls.calculate_order_price(
            data=data) + data.get("penalty")

        return data

    @classmethod
    def create(cls, *, data: OrderRequest, db: Generator, model: OrderModel):
        data = cls.prepare_data(data=data, db=db)
        cls.validation_class.validate(data)

        order = super().create(
            data=data,
            db=db,
            model=model,
        )

        if order:
            cls.update_order_film_availability(
                data=data,
                db=db,
                amount=-1,
            )

        return order

    @classmethod
    def update(cls, *, _id: int, data: FilmModel,
               db: Generator, model: OrderModel):
        data = cls.prepare_data(data=data, db=db)
        cls.validation_class.validate(data)

        order = super().update(
            _id=_id,
            data=data,
            db=db,
            model=model,
        )

        if order.returned:
            cls.update_order_film_availability(
                data=data,
                db=db,
                amount=1,
            )

        return order
