from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from .Base import Base  # Импортируем Base из base.py


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id", ondelete='CASCADE'))
    date = Column(String)  # Используем Date для хранения даты продажи
    total_amount = Column(Float)  # Общая сумма продажи

    # Связь с магазином
    store = relationship("Store", cascade="all, delete", back_populates="sales")

    # Связь с SaleItem для получения всех товаров в продаже
    items = relationship("SaleItem", cascade="all, delete", back_populates="sale")