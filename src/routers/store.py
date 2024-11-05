from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.stores.StoreCreate import StoreCreate
from models.stores.StoreResponse import StoreResponse

from CRUD.stores import create_store, get_store, update_store, delete_store, get_all_stores


router = APIRouter()


@router.post("/", response_model=StoreResponse)
def add_store(store: StoreCreate, db: Session = Depends(get_db)):
    return create_store(db=db, store=store)


@router.get("/{store_id}", response_model=StoreResponse)
def read_store(store_id: int, db: Session = Depends(get_db)):
    store = get_store(db=db, store_id=store_id)
    if store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@router.put("/{store_id}", response_model=StoreResponse)
def update_store_endpoint(store_id: int, store: StoreCreate, db: Session = Depends(get_db)):
    updated_store = update_store(db=db, store_id=store_id, store=store)
    if updated_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return updated_store


@router.delete("/{store_id}", response_model=StoreResponse)
def delete_store_endpoint(store_id: int, db: Session = Depends(get_db)):
    deleted_store = delete_store(db=db, store_id=store_id)
    if deleted_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return deleted_store


@router.get("/", response_model=list[StoreResponse])
def read_all_stores(db: Session = Depends(get_db)):
    return get_all_stores(db=db)