from pydantic import BaseModel, validator

from api.utils.validation.data_validation import DataValidation


class FilmCategoryRequest(BaseModel):
    category: str

    @validator('category')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)

    @validator('category')
    def field_not_numeric(cls, value):
        return DataValidation.field_not_numeric(value)


class FilmCategoryResponse(FilmCategoryRequest):
    id: int

    class Config:
        orm_mode = True
