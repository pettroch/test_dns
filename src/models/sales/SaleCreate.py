from pydantic import BaseModel
from typing import List

from models.sales.SaleItemCreate import SaleItemCreate


# Модель для создания и обновления продажи
class SaleCreate(BaseModel):
    store_id: int
    date: str
    total_amount: float
    items: List[SaleItemCreate]
