from pydantic import BaseModel, validator, EmailStr

from api.apps.users.schemas import UserRoleResponse
from api.utils.validation.data_validation import DataValidation


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserRequest(UserBase):
    password: str
    role_id: int

    @validator('username', 'email', 'password')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)


class UserResponse(UserBase):
    role: UserRoleResponse
    id: int

    class Config:
        orm_mode = True
