from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.apps.users.models import UserModel, UserRoleModel
from api.core.business import Business


class PermissionManager:
    @staticmethod
    def check_permission(*, user: UserModel,
                         role_required: str, db: Session) -> None:
        if role_required == Business.ANON_ROLE:
            return None

        role_obj = db.query(UserRoleModel).filter(
            UserRoleModel.role == role_required).first()

        if user.role.permission_level < role_obj.permission_level:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN.value,
                detail="Operation not allowed.",
            )
