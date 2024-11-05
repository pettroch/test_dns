from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    store_id = Column(Integer, ForeignKey("stores.id", ondelete='CASCADE'))  # Внешний ключ на магазин

    # Определите отношение между Product и Store
    store = relationship("Store", cascade="all, delete", back_populates="products")  # Обратное отношение
