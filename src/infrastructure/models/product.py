from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.infrastructure.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String(127), unique=True)
    measure = Column(String(15))
    code = Column(String(31))
    image_url = Column(String(255))

    # limit_item = relationship('LimitItem', back_populates='product')
