from http import HTTPStatus
from typing import Callable

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def catch_database_error(func: Callable) -> Callable:
    def catch(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as err:
            message = str(err.orig) + " for parameters" + str(err.params)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST.value,
                detail=message,
            )

    return catch
