from typing import Generator

from api.apps.users.models import UserModel
from api.core.security.hasher import Hasher
from api.db.base_class import Base
from api.db.managers.query_manager import QueryManager


class UserManager(QueryManager):

    @classmethod
    def prepare_data(cls, *, data: UserModel):
        data = data.dict()
        data["password"] = Hasher.hash_password(data.get("password"))

        return data

    @classmethod
    def create(cls, *, data: UserModel, db: Generator, model: Base):
        data = cls.prepare_data(data=data)

        return super().create(
            data=data,
            db=db,
            model=model,
        )

    @classmethod
    def update(cls, *, _id: int, data: UserModel, db: Generator, model: Base):
        data = cls.prepare_data(data=data)

        return super().update(
            _id=_id,
            data=data,
            db=db,
            model=model,
        )
