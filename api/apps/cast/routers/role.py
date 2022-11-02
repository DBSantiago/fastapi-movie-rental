from http import HTTPStatus

from fastapi import APIRouter, Depends

from api.apps.cast.models import RoleModel
from api.apps.cast.schemas import RoleRequest, RoleResponse
from api.apps.cast.services import CastAttrResponseManager
from api.dependencies.db import get_db
from api.dependencies.user import get_current_user

router = APIRouter(prefix="/roles", tags=["roles"])

_model = RoleModel
_request_schema = RoleRequest
_response_schema = RoleResponse
_service = CastAttrResponseManager


@router.get(
    path="/",
    response_model=list[_response_schema],
    status_code=HTTPStatus.OK.value,
)
async def get_all(db=Depends(get_db),
                  user=Depends(get_current_user)):
    return _service.get_all(
        db=db,
        model=_model,
        user=user,
        output_schema=_response_schema,
    )


@router.post(
    path="/",
    response_model=_response_schema,
    status_code=HTTPStatus.CREATED.value,
)
async def post(data: _request_schema, db=Depends(get_db),
               user=Depends(get_current_user)):
    return _service.create(
        data=data,
        db=db,
        model=_model,
        user=user,
        output_schema=_response_schema,
    )


@router.get(
    path="/{_id}",
    response_model=_response_schema,
    status_code=HTTPStatus.OK.value,
)
async def get(_id: int, db=Depends(get_db),
              user=Depends(get_current_user)):
    return _service.get_by_id(
        _id=_id,
        db=db,
        model=_model,
        user=user,
        output_schema=_response_schema,
    )


@router.put(
    path="/{_id}",
    response_model=_response_schema,
    status_code=HTTPStatus.OK.value,
)
async def put(_id: int, data: _request_schema, db=Depends(get_db),
              user=Depends(get_current_user)):
    return _service.update(
        _id=_id,
        data=data,
        db=db,
        model=_model,
        user=user,
        output_schema=_response_schema,
    )


@router.delete(
    path="/{_id}",
    status_code=HTTPStatus.NO_CONTENT.value,
)
async def delete(_id: int, db=Depends(get_db),
                 user=Depends(get_current_user)):
    return _service.destroy(
        _id=_id,
        db=db,
        model=_model,
        user=user,
    )
