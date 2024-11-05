from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city_id = Column(Integer, ForeignKey("cities.id", ondelete='CASCADE'))

    # Определите отношение между Store и Product
    products = relationship("Product", cascade="all, delete", back_populates="store")  # Обратное отношение

    # Связь с City
    city = relationship("City", cascade="all, delete", back_populates="stores")

    # Связь с Sale для получения всех продаж в магазине
    sales = relationship("Sale", cascade="all, delete", back_populates="store")