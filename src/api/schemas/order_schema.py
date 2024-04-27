from typing import List

from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    product_id: int
    count: int


class OrderCreate(BaseModel):
    user_id: int
    dmtt_id: int
    items: List[OrderItemCreate]
