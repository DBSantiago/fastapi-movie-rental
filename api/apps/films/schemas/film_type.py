from pydantic import BaseModel, validator

from api.utils.validation.data_validation import DataValidation


class FilmTypeRequest(BaseModel):
    film_type: str

    @validator('film_type')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)

    @validator('film_type')
    def field_not_numeric(cls, value):
        return DataValidation.field_not_numeric(value)


class FilmTypeResponse(FilmTypeRequest):
    id: int

    class Config:
        orm_mode = True
