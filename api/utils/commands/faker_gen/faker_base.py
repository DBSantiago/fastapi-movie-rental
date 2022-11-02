from typing import Any, Union

from sqlalchemy.exc import SQLAlchemyError, PendingRollbackError

from api.db.base_class import Base
from api.db.session import SessionLocal
from api.utils.logger import Logger

logger = Logger.get_logger_console("FakerBaseLog")


class FakerBase:
    """Base class for generating database records with Faker."""
    records = 10
    model = None

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        raise NotImplementedError

    @classmethod
    def generate_single_record(cls, *args,
                               **kwargs) -> Union[Base, None]:
        fields = cls.set_up()
        with SessionLocal() as db:

            try:
                obj = cls.model(**fields, **kwargs)
                db.add(obj)
                db.commit()
                db.refresh(obj)
                return obj
            except (SQLAlchemyError, PendingRollbackError):
                logger.error("An error occurred. Skipping...")
                db.rollback()

    @classmethod
    def generate_records(cls) -> None:
        for _ in range(cls.records):
            cls.generate_single_record()
