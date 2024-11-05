import uvicorn
from fastapi import FastAPI

#from database import db
from database.init_db import init_db

from routers import product, city, store, sale


app = FastAPI()
app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(city.router, prefix="/cities", tags=["cities"])
app.include_router(store.router, prefix="/stores", tags=["stores"])
app.include_router(sale.router, prefix="/sales", tags=["sales"])


if __name__ == "__main__":
    init_db()
    uvicorn.run("app:app", port=5000, log_level="info")
