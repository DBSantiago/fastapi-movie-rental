from http import HTTPStatus

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from api.core.config import Settings
from api.core.security.authentication.login_manager import LoginManager
from api.core.security.tokens.token_schema import TokenData
from api.dependencies.db import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme),
                           db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED.value,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token,
                             Settings.SECRET_KEY,
                             algorithms=[Settings.HASH_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = LoginManager.get_user(token_data.username, db)

    if user is None:
        raise credentials_exception

    return user
