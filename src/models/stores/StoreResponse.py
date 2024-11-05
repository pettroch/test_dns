from pydantic import BaseModel


# Модель для ответа с данными о магазине
class StoreResponse(BaseModel):
    id: int
    name: str
    city_id: int

    class Config:
        orm_mode = True