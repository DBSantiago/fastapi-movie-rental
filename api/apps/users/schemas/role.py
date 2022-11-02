from pydantic import BaseModel, validator

from api.utils.validation.data_validation import DataValidation


class UserRoleRequest(BaseModel):
    role: str
    permission_level: int

    @validator('role')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)

    @validator('role')
    def field_not_numeric(cls, value):
        return DataValidation.field_not_numeric(value)


class UserRoleResponse(UserRoleRequest):
    id: int

    class Config:
        orm_mode = True
