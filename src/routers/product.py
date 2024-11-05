from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.products.ProductCreate import ProductCreate
from models.products.ProductResponse import ProductResponse

from CRUD.products import create_product, get_product, update_product, delete_product, get_all_products


router = APIRouter()

@router.post("/", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)


@router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    updated_product = update_product(db=db, product_id=product_id, product=product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    deleted_product = delete_product(db=db, product_id=product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product


@router.get("/", response_model=list[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    return get_all_products(db=db)