from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.api.schemas.product import ProductCreate
from src.domain.exceptions import not_found_exception
from src.infrastructure.models.product import Product
from src.infrastructure.repositories.dmtt_repo import DmttRepo
from src.infrastructure.services.excel_service import SheetDataFetcher


class LimitService():
    def __init__(self) -> None:
        self._sheet_data_fetcher = SheetDataFetcher()
        self._dmtt_repo = DmttRepo()

    async def get_limit_by_dmtt(self, manager):
        dmtt_instance = await self._dmtt_repo.filter_one(user_id=manager.id)
        if not dmtt_instance:
            raise not_found_exception("Dmtt")
        data = await self._sheet_data_fetcher.get_data(sheet_url=dmtt_instance.excel_url, sheet_name=dmtt_instance.active_sheet_name)
        return data
