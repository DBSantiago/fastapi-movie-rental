from typing import Union, Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.apps.users.models import UserModel
from api.core.security.permissions import PermissionManager, MethodPermissions
from api.db.base_class import Base
from api.utils.responses.response_standard import response_standard


class ResponseManager:
    query_manager = None
    method_permissions = MethodPermissions.ANON

    @classmethod
    @response_standard("POST")
    def create(cls, *, data: Union[BaseModel, dict],
               db: Session, model: Base, user: Optional[UserModel],
               output_schema: BaseModel):
        PermissionManager.check_permission(
            user=user,
            role_required=cls.method_permissions.get("POST"),
            db=db
        )

        response_data = cls.query_manager.create(
            data=data,
            db=db,
            model=model
        )

        serialized_data = output_schema.from_orm(response_data)

        return serialized_data

    @classmethod
    @response_standard("PUT")
    def update(cls, *, _id: int, data: Union[BaseModel, dict],
               db: Session, model: Base, user: Optional[UserModel],
               output_schema: BaseModel):
        PermissionManager.check_permission(
            user=user,
            role_required=cls.method_permissions.get("PUT"),
            db=db
        )

        response_data = cls.query_manager.update(
            _id=_id,
            data=data,
            db=db,
            model=model
        )

        serialized_data = output_schema.from_orm(response_data)

        return serialized_data

    @classmethod
    @response_standard("GET")
    def get_by_id(cls, *, _id: int, db: Session,
                  model: Base, user: Optional[UserModel],
                  output_schema: BaseModel):
        PermissionManager.check_permission(
            user=user,
            role_required=cls.method_permissions.get("GET"),
            db=db
        )

        response_data = cls.query_manager.get_by_id(
            _id=_id,
            db=db,
            model=model
        )

        serialized_data = output_schema.from_orm(response_data)

        return serialized_data

    @classmethod
    @response_standard("GET")
    def get_all(cls, *, db: Session,
                model: Base, user: Optional[UserModel],
                output_schema: BaseModel):
        PermissionManager.check_permission(
            user=user,
            role_required=cls.method_permissions.get("GET"),
            db=db
        )

        response_data = cls.query_manager.get_all(
            db=db,
            model=model
        )

        serialized_data = [output_schema.from_orm(obj) for obj
                           in response_data]

        return serialized_data

    @classmethod
    @response_standard("DELETE")
    def destroy(cls, *, _id: int, db: Session,
                model: Base, user: Optional[UserModel]):
        PermissionManager.check_permission(
            user=user,
            role_required=cls.method_permissions.get("DELETE"),
            db=db
        )

        response_data = cls.query_manager.destroy(
            _id=_id,
            db=db,
            model=model
        )

        return response_data
