from pydantic import BaseModel


# Модель для создания и обновления товара
class ProductCreate(BaseModel):
    name: str
    price: float
    store_id: int
