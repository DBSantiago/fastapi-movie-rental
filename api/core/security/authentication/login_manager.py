from datetime import timedelta
from http import HTTPStatus
from typing import Union

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.apps.users.models import UserModel
from api.core.config import Settings
from api.core.security.hasher import Hasher
from api.core.security.tokens.token_manager import TokenManager
from api.core.security.tokens.token_schema import Token


class LoginManager:
    @staticmethod
    def get_user(username: str, db: Session) -> UserModel:
        user = db.query(UserModel).filter(
            UserModel.username == username).first()

        return user

    @classmethod
    def authenticate_user(cls, username: str,
                          password: str,
                          db: Session) -> Union[UserModel, bool]:
        user = cls.get_user(username, db)
        if not user:
            return False

        if not Hasher.verify_password(password, user.password):
            return False

        return user

    @classmethod
    def login_for_access_token(cls, *,
                               form_data: OAuth2PasswordRequestForm,
                               db: Session) -> Token:
        user = cls.authenticate_user(
            form_data.username, form_data.password, db)

        if not user:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED.value,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(
            minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = TokenManager.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return Token(access_token=access_token, token_type="bearer")
