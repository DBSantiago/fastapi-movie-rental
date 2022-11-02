from datetime import date
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException

from api.core.business import Business


class OrderValidator:
    """Class for validating an Order's data."""

    @staticmethod
    def rent_time_not_exceeded(start_date, end_date) -> None:
        """Validate if rent time is longer than 15 days."""
        date_diff = end_date - start_date

        if date_diff.days >= Business.MAX_RENT_DAYS:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail="Stipulated return date can't be higher than 15 days.",
            )

    @staticmethod
    def return_date_in_future(return_date) -> None:
        """Validate if rent return date is not a past date."""
        if return_date < date.today():
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail="Stipulated return date can't be in the past.",
            )

    @staticmethod
    def film_is_available(film) -> None:
        """Validate if a film has copies available."""
        if not film.availability:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail=f"We don't have enough copies of {film} available.",
            )

    @classmethod
    def validate(cls, order: dict[str, Any]):
        cls.return_date_in_future(order.get("return_date"))
        cls.rent_time_not_exceeded(
            order.get("rent_date"), order.get("return_date"))

        for film in order.get("films"):
            cls.film_is_available(film)
