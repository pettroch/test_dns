from pydantic import BaseModel


# Модель для ответа с данными о товаре
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True
