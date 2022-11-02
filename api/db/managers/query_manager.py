from http import HTTPStatus
from typing import Generator, Any, Union

from fastapi import HTTPException
from pydantic import BaseModel

from api.db.base_class import Base
from api.db.exceptions.catch_database_error import catch_database_error


class QueryManager:

    @classmethod
    def get_nested_model(cls, data: dict[str, Any], field: str,
                         model: Base, db: Generator):
        obj_id_list = data.get(field)

        return [cls.get_by_id(_id=obj_id, db=db, model=model)
                for obj_id in obj_id_list]

    @staticmethod
    def get_by_id(*, _id: int, db: Generator, model: Base):
        obj = db.query(model).filter(model.id == _id).first()

        if not obj:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND.value,
                detail=f"{model.__name__.strip('Model')} object "
                       f"with id: {_id} not found.",
            )

        return obj

    @staticmethod
    def get_all(*, db: Generator, model: Base):
        return db.query(model).all()

    @staticmethod
    @catch_database_error
    def create(*, data: Union[BaseModel, dict], db: Generator, model: Base):
        if not isinstance(data, dict):
            data = data.dict()

        obj = model(**data)

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    @classmethod
    @catch_database_error
    def update(cls, *, _id: int, data: Union[BaseModel, dict],
               db: Generator, model: Base):
        obj = cls.get_by_id(
            _id=_id,
            db=db,
            model=model,
        )

        if not isinstance(data, dict):
            data = data.dict()

        for field, value in data.items():
            setattr(obj, field, value)

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    @classmethod
    @catch_database_error
    def destroy(cls, *, _id: int, db: Generator, model: Base):
        obj = cls.get_by_id(
            _id=_id,
            db=db,
            model=model,
        )

        db.delete(obj)
        db.commit()

        return None
