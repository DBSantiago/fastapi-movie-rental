from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.core.security.authentication.login_manager import LoginManager
from api.core.security.tokens.token_schema import Token
from api.dependencies.db import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)) -> Token:
    return LoginManager.login_for_access_token(
        form_data=form_data,
        db=db,
    )
