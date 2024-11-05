from pydantic import BaseModel


# Модель для ответа с данными о городе
class CityResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
