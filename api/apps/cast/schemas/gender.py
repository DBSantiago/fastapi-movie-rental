from pydantic import BaseModel, validator

from api.utils.validation.data_validation import DataValidation


class GenderRequest(BaseModel):
    gender: str

    @validator('gender')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)


class GenderResponse(GenderRequest):
    id: int

    class Config:
        orm_mode = True
