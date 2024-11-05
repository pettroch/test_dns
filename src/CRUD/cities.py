from sqlalchemy.orm import Session
from database.schemes.City import City  # Импортируйте вашу SQLAlchemy модель
from models.cities.CityCreate import CityCreate
from models.cities.CityResponse import CityResponse


def create_city(db: Session, city: CityCreate) -> CityResponse:
    db_city = City(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)  # Получаем сгенерированный ID

    return CityResponse(id=db_city.id, name=db_city.name)


def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


def update_city(db: Session, city_id: int, city: CityCreate):
    db_city = get_city(db=db, city_id=city_id)
    if db_city:
        for key, value in city.model_dump().items():  # Используем model_dump()
            setattr(db_city, key, value)
        db.commit()
        db.refresh(db_city)
    return db_city


def delete_city(db: Session, city_id: int):
    db_city = get_city(db=db, city_id=city_id)
    if db_city:
        db.delete(db_city)
        db.commit()
    return db_city


def get_all_cities(db: Session):
    return db.query(City).all()