from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from src.api.schemas.company_schema import (CompanyCreate, CompanyInfo,
                                            CompanyUpdate)
from src.dependencies import get_current_user
from src.services.company_service import CompanyService
from src.services.user_service import UsersService

service = CompanyService()

user_service = UsersService()
router = APIRouter(tags=["Firma"])


@router.get("/companies", response_model=List[CompanyInfo], response_class=ORJSONResponse)
async def get_all_company(tg_user_id: str):
    user = user_service(tg_user_id)
    return await service.get_all_companies()


@router.get("/companies/{id}", response_model=CompanyInfo)
async def get_company(tg_user_id, id: int):
    user = user_service(tg_user_id)
    return await service.get_company_by_id(id=id)


@router.post("/companies/", response_model=CompanyInfo)
async def create(tg_user_id: str, data: CompanyCreate, user=Depends(get_current_user)):
    user = user_service(tg_user_id)
    return await service.create_company(data=data)


@router.put("/companies/{id}/", response_model=CompanyInfo)
async def update_company(id: int, tg_user_id: str, data: CompanyUpdate):
    user = user_service(tg_user_id)
    return await service.update_company(id=id, data=data)


@router.delete("/{id}")
async def delete_company(id: int, tg_user_id: str):
    user = user_service(tg_user_id)
    return await service.delete_company(id=id)
