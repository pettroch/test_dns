from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.cities.CityCreate import CityCreate
from models.cities.CityResponse import CityResponse

from CRUD.cities import create_city, get_city, update_city, delete_city, get_all_cities


router = APIRouter()


@router.post("/", response_model=CityResponse)
def add_city(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db=db, city=city)


@router.get("/{city_id}", response_model=CityResponse)
def get_city_by_id(city_id: int, db: Session = Depends(get_db)):
    db_city = get_city(db=db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city


@router.put("/{city_id}", response_model=CityResponse)
def update_city_by_id(city_id: int, city: CityCreate, db: Session = Depends(get_db)):
    db_city = update_city(db=db, city_id=city_id, city=city)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city


@router.delete("/{city_id}", response_model=CityResponse)
def delete_city_by_id(city_id: int, db: Session = Depends(get_db)):
    db_city = delete_city(db=db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city


@router.get("/", response_model=List[CityResponse])
def get_cities(db: Session = Depends(get_db)):
    return get_all_cities(db=db)