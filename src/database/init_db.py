from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schemes.Base import Base
from .schemes.City import City
from .schemes.Product import Product
from .schemes.Store import Store
from .schemes.Sale import Sale
from .schemes.SaleItem import SaleItem


DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/test_dns"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
