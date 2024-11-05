from sqlalchemy.orm import Session
from typing import List

from database.schemes.Product import Product  # Импортируйте вашу SQLAlchemy модель
from models.products.ProductCreate import ProductCreate
from models.products.ProductResponse import ProductResponse
from database.schemes.SaleItem import SaleItem


def create_product(db: Session, product: ProductCreate) -> ProductResponse:
    db_product = Product(name=product.name, price=product.price, store_id=product.store_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # Получаем сгенерированный ID

    return ProductResponse(id=db_product.id, name=db_product.name, price=db_product.price)


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db=db, product_id=product_id)
    if db_product:
        for key, value in product.model_dump().items():  # Используем model_dump()
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    # Сначала удаляем все связанные записи из sale_items
    db.query(SaleItem).filter(SaleItem.product_id == product_id).delete()
    
    # Теперь удаляем продукт
    product_to_delete = db.query(Product).filter(Product.id == product_id).first()
    
    
    db.delete(product_to_delete)
    db.commit()
    return product_to_delete


def get_all_products(db: Session):
    return db.query(Product).all()