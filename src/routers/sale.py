from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database.db import get_db

from models.sales.SaleCreate import SaleCreate
from models.sales.SaleResponse import SaleResponse
from models.sales.SaleItemResponse import SaleItemResponse

from CRUD.sales import get_sales_by_city, create_sale, get_sales_by_store, get_sales_by_product, get_sales_last_n_days, get_sales_above_n_amount, get_sales_below_n_amount, get_sales_with_quantity_above_n, get_sales_with_quantity_below_n, get_sale_by_id, update_sale, delete_sale, get_all_sales, get_sale


router = APIRouter()


@router.post("/", response_model=SaleResponse)
def add_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db=db, sale=sale)


@router.get("/city/{city_id}", response_model=List[SaleResponse])
def read_sales_by_city(city_id: int, db: Session = Depends(get_db)):
    return get_sales_by_city(db=db, city_id=city_id)


@router.get("/store/{store_id}", response_model=List[SaleItemResponse])
def read_sales_by_store(store_id: int, db: Session = Depends(get_db)):
    sales = get_sales_by_store(db=db, store_id=store_id)  # Передаем store_id в функцию
    return sales


@router.get("/product/{product_id}", response_model=List[SaleItemResponse])
def read_sales_by_product(product_id: int, db: Session = Depends(get_db)):
    sales = get_sales_by_product(db=db, product_id=product_id)
    return sales


@router.get("/last_days", response_model=List[SaleItemResponse])
async def read_sales_last_n_days(n_days: int = Query(...), db: Session = Depends(get_db)):
    sales = get_sales_last_n_days(db=db, n_days=n_days)
    return sales


@router.get("/above/{n_amount}", response_model=List[SaleItemResponse])
def read_sales_above_amount(n_amount: float, db: Session = Depends(get_db)):
    sales = get_sales_above_n_amount(db, n_amount)
    
    if not sales:
        raise HTTPException(status_code=404, detail="Продаж с такой суммой не найдено.")
    
    return sales


@router.get("/below/{n_amount}", response_model=List[SaleItemResponse])
def read_sales_below_amount(n_amount: float, db: Session = Depends(get_db)):
    sales = get_sales_below_n_amount(db, n_amount)
    
    if not sales:
        raise HTTPException(status_code=404, detail="Продаж с такой суммой не найдено.")
    
    return sales


@router.get("/quantity_above/{n_quantity}", response_model=List[SaleItemResponse])
def get_sales_above_quantity(n_quantity: int, db: Session = Depends(get_db)):
    return get_sales_with_quantity_above_n(db, n_quantity)


@router.get("/quantity_below/{n_quantity}", response_model=List[SaleItemResponse])
def get_sales_below_quantity(n_quantity: int, db: Session = Depends(get_db)):
    return get_sales_with_quantity_below_n(db, n_quantity)


@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = get_sale_by_id(db, sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


@router.get("/{sale_id}", response_model=SaleResponse)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = get_sale(db=db, sale_id=sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


@router.put("/{sale_id}", response_model=SaleResponse)
def update_sale_endpoint(sale_id: int, sale: SaleCreate, db: Session = Depends(get_db)):
    updated_sale = update_sale(db=db, sale_id=sale_id, sale=sale)
    if updated_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated_sale


@router.delete("/{sale_id}", response_model=SaleResponse)
def delete_sale_endpoint(sale_id: int, db: Session = Depends(get_db)):
    deleted_sale = delete_sale(db=db, sale_id=sale_id)
    if deleted_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return deleted_sale


@router.get("/", response_model=list[SaleResponse])
def read_all_sales(db: Session = Depends(get_db)):
    return get_all_sales(db=db)