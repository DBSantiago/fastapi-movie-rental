from pydantic import BaseModel, validator, EmailStr

from api.utils.validation.data_validation import DataValidation


class CustomerRequest(BaseModel):
    name: str
    last_name: str
    email: EmailStr

    @validator('name', 'last_name', 'email')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)

    @validator('name', 'last_name')
    def field_not_numeric(cls, value):
        return DataValidation.field_not_numeric(value)


class CustomerResponse(CustomerRequest):
    id: int

    class Config:
        orm_mode = True
