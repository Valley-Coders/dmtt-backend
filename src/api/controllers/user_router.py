
from typing import List

from fastapi import APIRouter, Depends

from src.api.schemas.user_schema import UserInfo
from src.dependencies import get_current_user
from src.domain.models.user_model import UserCreate
from src.services.user_service import UsersService

service = UsersService()

router = APIRouter(tags=["Users"])


@router.post("/users/")
async def create_manager(data: UserCreate):
    return await service.create_user(data=data)


@router.get("/users", response_model=List[UserInfo])
async def create_manager():
    return await service.get_all_users()


@router.get("/profile", response_model=UserInfo)
async def get_my_profile(user=Depends(get_current_user)):
    return user
