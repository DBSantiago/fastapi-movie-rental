from datetime import date
from http import HTTPStatus
from typing import Any

from fastapi import HTTPException


class FilmValidator:
    @staticmethod
    def stock_greater_than_availability(film: dict[str, Any]) -> None:
        if film.get("availability") > film.get("stock"):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail="Film availability cannot be higher than stock.",
            )

    @staticmethod
    def release_date_in_the_past(film: dict[str, Any]) -> None:
        if date.today() < film.get("release_date"):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail="Film release date cannont be in the future.",
            )

    @classmethod
    def validate(cls, film: dict[str, Any]) -> None:
        cls.stock_greater_than_availability(film)
        cls.release_date_in_the_past(film)
