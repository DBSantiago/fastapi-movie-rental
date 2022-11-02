from pydantic import BaseModel, validator

from api.utils.validation.data_validation import DataValidation


class RoleRequest(BaseModel):
    role: str

    @validator('role')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)


class RoleResponse(RoleRequest):
    id: int

    class Config:
        orm_mode = True
