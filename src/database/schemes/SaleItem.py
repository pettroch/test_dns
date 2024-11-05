from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from .Base import Base  # Импортируем Base из base.py


class SaleItem(Base):
    __tablename__ = "sale_items"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id", ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey("products.id", ondelete='CASCADE'))
    quantity = Column(Integer)  # Количество проданного товара
    price = Column(Float)  # Цена товара на момент продажи
    total_price = Column(Float)  # Общая цена за все проданные единицы

    # Связь с таблицей продаж
    sale = relationship("Sale", cascade="all, delete", back_populates="items")

    # Связь с таблицей товаров
    product = relationship("Product", cascade="all, delete")
