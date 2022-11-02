from datetime import date
from decimal import Decimal

from pydantic import BaseModel, validator

from api.apps.cast.schemas import MemberResponse
from api.apps.films.schemas import (
    FilmCategoryResponse, FilmTypeResponse,
)
from api.utils.validation.data_validation import DataValidation


class FilmBase(BaseModel):
    title: str
    description: str
    price: Decimal
    stock: int
    availability: int
    release_date: date


class FilmRequest(FilmBase):
    film_type_id: int
    categories: list[int]
    cast: list[int]

    @validator('title', 'description')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)

    @validator('price', 'stock', 'availability')
    def field_positive_number(cls, value):
        return DataValidation.field_positive_number(value)


class FilmResponse(FilmBase):
    id: int
    film_type: FilmTypeResponse
    categories: list[FilmCategoryResponse]
    cast: list[MemberResponse]

    class Config:
        orm_mode = True
