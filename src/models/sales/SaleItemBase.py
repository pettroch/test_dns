from pydantic import BaseModel


class SaleItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float
    total_price: float
