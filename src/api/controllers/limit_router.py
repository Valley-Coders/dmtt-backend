
from fastapi import APIRouter, Depends

from src.dependencies import get_current_manager
from src.services.limit_service import LimitService

router = APIRouter()
limit_service = LimitService()


@router.get("/limit")
async def get_limit_dmtt(manager=Depends(get_current_manager)):
    return await limit_service.get_limit_by_dmtt(
        manager=manager
    )
