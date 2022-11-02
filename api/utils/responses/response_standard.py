from http import HTTPStatus
from typing import Callable

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from api.utils.logger import Logger

_code_for_method = {
    "GET": HTTPStatus.OK.value,
    "POST": HTTPStatus.CREATED.value,
    "PUT": HTTPStatus.OK.value,
    "DELETE": HTTPStatus.NO_CONTENT.value,
}

logger = Logger.get_logger_console(__name__)


def response_standard(method: str) -> Callable:
    """Standardize HTTP response in JSend format."""

    def standardize(func: Callable) -> Callable:

        def wrapper(*args, **kwargs):
            try:
                response = func(*args, **kwargs)
                if response:
                    if type(response) == list:
                        response = [schema.dict() for schema in response]
                    else:
                        response.dict()
                status = "success"
                code = _code_for_method.get(method.upper())
            except HTTPException as err:
                response = err.detail
                status = "fail"
                code = err.status_code
            except Exception as err:
                logger.error(err)
                response = "Something went horribly wrong!"
                status = "error"
                code = HTTPStatus.INTERNAL_SERVER_ERROR

            standard = {
                "status": status,
                "data": jsonable_encoder(response)
            }

            new_response = JSONResponse(
                content=standard,
                status_code=code,
            )

            return new_response

        return wrapper

    return standardize
