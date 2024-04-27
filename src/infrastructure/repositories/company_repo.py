from typing import Any, Coroutine, Type

from pydantic import BaseModel
from pydantic.main import BaseModel

from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models.company import Company
from src.infrastructure.repositories.base import CRUDRepoBase


class CompanyRepo(CRUDRepoBase):
    model = Company

    async def create(self, user_id: int, obj_in: type[BaseModel]) -> Coroutine[Any, Any, BaseModel]:
        with get_db() as session:
            new_obj = self.model(**obj_in.model_dump(), user_id=user_id)
            session.add(new_obj)
            session.commit()
            session.refresh(new_obj)
            return new_obj
