from sqlalchemy.orm import Session
from database.schemes.Store import Store  # Импортируйте вашу SQLAlchemy модель
from models.stores.StoreCreate import StoreCreate
from models.stores.StoreResponse import StoreResponse


def create_store(db: Session, store: StoreCreate) -> StoreResponse:
    db_store = Store(name=store.name, city_id=store.city_id)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)  # Получаем сгенерированный ID

    return StoreResponse(id=db_store.id, name=db_store.name, city_id=db_store.city_id)


def get_store(db: Session, store_id: int):
    return db.query(Store).filter(Store.id == store_id).first()


def update_store(db: Session, store_id: int, store: StoreCreate):
    db_store = get_store(db=db, store_id=store_id)
    if db_store:
        for key, value in store.model_dump().items():  # Используем model_dump()
            setattr(db_store, key, value)
        db.commit()
        db.refresh(db_store)
    return db_store


def delete_store(db: Session, store_id: int):
    db_store = get_store(db=db, store_id=store_id)
    if db_store:
        db.delete(db_store)
        db.commit()
    return db_store


def get_all_stores(db: Session):
    return db.query(Store).all()