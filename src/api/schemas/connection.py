from typing import List

from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError


class ConnectionBase(BaseModel):
    product_id: int = Field()
    company_id: int
    dmtt_id: int


class ConnectionCreate(ConnectionBase):
    pass


class ConnectionInfo(ConnectionBase):
    id: int

    class ConfigDict:
        from_attributes = True


class ConnectionItem(BaseModel):
    dmtt_id: int
    product_id: int


class CompanyConnectionCreate(BaseModel):
    company_id: int
    items: List[ConnectionItem]
