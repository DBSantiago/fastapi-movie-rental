from pydantic import BaseModel, validator

from api.apps.cast.schemas import GenderResponse, RoleResponse
from api.utils.validation.data_validation import DataValidation


class MemberBase(BaseModel):
    name: str
    last_name: str


class MemberRequest(MemberBase):
    gender_id: int
    role_id: int

    @validator('name', 'last_name')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)

    @validator('name', 'last_name')
    def field_not_numeric(cls, value):
        return DataValidation.field_not_numeric(value)


class MemberResponse(MemberBase):
    id: int
    gender: GenderResponse
    role: RoleResponse

    class Config:
        orm_mode = True
