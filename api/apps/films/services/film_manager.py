from typing import Generator

from api.apps.cast.models import MemberModel
from api.apps.films.models import FilmModel, FilmCategoryModel
from api.apps.films.services.film_validator import FilmValidator
from api.db.base_class import Base
from api.db.managers.query_manager import QueryManager


class FilmManager(QueryManager):
    validation_class = FilmValidator

    @classmethod
    def prepare_data(cls, *, data: FilmModel, db: Generator):
        data = data.dict()
        data["categories"] = cls.get_nested_model(data=data,
                                                  field="categories",
                                                  model=FilmCategoryModel,
                                                  db=db)
        data["cast"] = cls.get_nested_model(data=data,
                                            field="cast",
                                            model=MemberModel,
                                            db=db)

        return data

    @classmethod
    def create(cls, *, data: FilmModel, db: Generator, model: Base):
        cls.validation_class.validate(data.dict())
        data = cls.prepare_data(data=data, db=db)

        return super().create(
            data=data,
            db=db,
            model=model,
        )

    @classmethod
    def update(cls, *, _id: int, data: FilmModel, db: Generator, model: Base):
        cls.validation_class.validate(data.dict())
        data = cls.prepare_data(data=data, db=db)

        return super().update(
            _id=_id,
            data=data,
            db=db,
            model=model,
        )
