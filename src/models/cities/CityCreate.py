from pydantic import BaseModel


# Модель для создания и обновления города
class CityCreate(BaseModel):
    name: str
