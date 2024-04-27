from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.api.schemas.token import TokenPayload
from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.user import User, UserRoleEnum
from src.infrastructure.repositories.jwt_token_repo import JWTTokenRepo
from src.infrastructure.services.token_service import TokenService

_token_service = TokenService()
_jwt_token_repo = JWTTokenRepo()

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/auth/swagger/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)):
    try:
        payload = jwt.decode(
            token, _token_service.SECRET_KEY, algorithms=[
                _token_service.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await _jwt_token_repo.get_user(token_data.jti)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user


async def get_admin(user: User = Depends(get_current_user)):
    if user.is_admin:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You don't have permission to access this resource",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_manager(user: User = Depends(get_current_user)):
    if user.role == UserRoleEnum.manager:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You don't have permission to access this resource",
        headers={"WWW-Authenticate": "Bearer"},
    )
