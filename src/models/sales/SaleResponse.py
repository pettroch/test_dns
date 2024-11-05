from pydantic import BaseModel
from typing import List

from models.sales.SaleItemResponse import SaleItemResponse


# Модель для ответа с данными о продаже
class SaleResponse(BaseModel):
    id: int
    store_id: int
    date: str
    total_amount: float
    items: List[SaleItemResponse]

    class Config:
        orm_mode = True
        from_attributes = True
        