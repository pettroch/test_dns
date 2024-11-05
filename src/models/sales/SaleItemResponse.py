from models.sales.SaleItemBase import SaleItemBase


class SaleItemResponse(SaleItemBase):
    id: int

    class Config:
        orm_mode = True  # Включите режим ORM
        from_attributes = True