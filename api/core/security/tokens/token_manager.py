from datetime import datetime, timedelta

from jose import jwt

from api.core.config import Settings


class TokenManager:
    @staticmethod
    def create_access_token(data: dict,
                            expires_delta: timedelta | None = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode,
                                 Settings.SECRET_KEY,
                                 algorithm=Settings.HASH_ALGORITHM)

        return encoded_jwt
