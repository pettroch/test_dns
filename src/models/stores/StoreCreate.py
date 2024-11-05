from pydantic import BaseModel


# Модель для создания и обновления магазина
class StoreCreate(BaseModel):
    name: str
    city_id: int