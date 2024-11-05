from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Определите отношение между City и Store
    stores = relationship("Store", cascade="all, delete", back_populates="city")  # Здесь указываем обратное отношение