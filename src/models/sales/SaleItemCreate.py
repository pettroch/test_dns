from pydantic import BaseModel


class SaleItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float
    total_price: float