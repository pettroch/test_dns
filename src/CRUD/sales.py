from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from typing import List, Optional

from database.schemes.Sale import Sale
from database.schemes.SaleItem import SaleItem
from database.schemes.Store import Store
from models.sales.SaleCreate import SaleCreate
from models.sales.SaleResponse import SaleResponse
from models.sales.SaleItemResponse import SaleItemResponse


def create_sale(db: Session, sale: SaleCreate):
    db_sale = Sale(
        store_id=sale.store_id, date=sale.date, total_amount=sale.total_amount
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)

    # Добавляем элементы продажи
    for item in sale.items:
        sale_item = SaleItem(
            sale_id=db_sale.id,  # Присваиваем sale_id, чтобы связать элемент с продажей
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.total_price,
        )
        db.add(sale_item)  # Добавляем элемент продажи в сессию

    db.commit()  # Коммитим изменения для сохранения элементов продажи

    return db_sale


def get_sales_by_city(db: Session, city_id: int):
    # Получаем магазины в заданном городе
    stores = db.query(Store).filter(Store.city_id == city_id).all()
    # Получаем продажи по магазинам
    sales = (
        db.query(Sale).filter(Sale.store_id.in_([store.id for store in stores])).all()
    )

    # Формируем ответ с учетом элементов продажи
    sales_response = []
    for sale in sales:
        sale_items = (
            db.query(SaleItem).filter(SaleItem.sale_id == sale.id).all()
        )  # Получаем элементы продажи для этой продажи
        items_response = [
            SaleItemResponse.from_orm(item) for item in sale_items
        ]  # Преобразуем их в SaleItemResponse
        sales_response.append(
            SaleResponse(
                id=sale.id,
                store_id=sale.store_id,
                date=sale.date,
                total_amount=sale.total_amount,
                items=items_response,  # Добавляем элементы продажи в ответ
            )
        )

    return sales_response


def get_sales_by_store(db: Session, store_id: int) -> List[SaleItemResponse]:
    # Получаем все продажи по конкретному магазину
    sales = db.query(Sale).filter(Sale.store_id == store_id).all()
    sale_items = []

    for sale in sales:
        for item in sale.items:
            sale_items.append(
                SaleItemResponse(
                    id=item.id,  # ID товара в продаже
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=item.price,
                    total_price=item.total_price,
                )
            )
    return sale_items


def get_sales_last_n_days(db: Session, n_days: int) -> List[SaleItemResponse]:
    today = datetime.now().date()  # Получаем текущую дату без времени
    start_date = today - timedelta(days=n_days - 1)  # Начало диапазона (включительно)

    # Получаем все продажи
    sales = db.query(Sale).all()

    filtered_sales = []
    for sale in sales:
        try:
            # Преобразуем строку в дату без времени
            sale_date = datetime.strptime(sale.date, "%d.%m.%Y").date()
        except ValueError as e:
            print(f"Ошибка преобразования даты {sale.date}: {e}")
            continue

        # Проверяем, попадает ли дата продажи в указанный диапазон
        if start_date <= sale_date <= today:
            filtered_sales.append(sale)

    # Создаем список SaleItemResponse на основе элементов sale
    sale_items_responses = []
    for sale in filtered_sales:
        for item in sale.items:
            sale_items_responses.append(
                SaleItemResponse(
                    id=item.id,  # Передаем поле id
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=item.price,
                    total_price=item.total_price,
                )
            )

    return sale_items_responses


def get_sales_by_product(db: Session, product_id: int) -> List[SaleItemResponse]:
    # Получаем все продажи для указанного товара
    sale_items = db.query(SaleItem).filter(SaleItem.product_id == product_id).all()
    return [SaleItemResponse.model_validate(item) for item in sale_items]


def get_sales_above_n_amount(db: Session, n_amount: float) -> List[SaleItemResponse]:
    sales = (
        db.query(Sale).filter(Sale.total_amount > n_amount).all()
    )  # Фильтрация по сумме
    for s in sales:
        print(f"{s.id}!!!!!!")
    return [
        SaleItemResponse(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.total_price,
        )
        for sale in sales
        for item in sale.items
    ]


def get_sales_below_n_amount(db: Session, n_amount: float) -> List[SaleItemResponse]:
    sales = (
        db.query(Sale).filter(Sale.total_amount < n_amount).all()
    )  # Фильтрация по сумме

    return [
        SaleItemResponse(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.total_price,
        )
        for sale in sales
        for item in sale.items
    ]


def get_sales_with_quantity_above_n(db: Session, n_quantity: int) -> List[SaleItemResponse]:
    sales_items = (
        db.query(SaleItem).filter(SaleItem.quantity > n_quantity).all()
    )  # Фильтрация по количеству товаров

    return [
        SaleItemResponse(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.total_price,
        )
        for item in sales_items
    ]


def get_sales_with_quantity_below_n(db: Session, n_quantity: int) -> List[SaleItemResponse]:
    sales_items = (
        db.query(SaleItem).filter(SaleItem.quantity < n_quantity).all()
    )  # Фильтрация по количеству товаров

    return [
        SaleItemResponse(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.total_price,
        )
        for item in sales_items
    ]


def get_sale_by_id(db: Session, sale_id: int) -> Optional[SaleResponse]:
    sale = db.query(Sale).filter(Sale.id == sale_id).first()  # Поиск по идентификатору

    if sale is None:
        return None

    # Преобразование найденной продажи в SaleResponse
    sale_items_responses = [
        SaleItemResponse(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            total_price=item.total_price,
        )
        for item in sale.items
    ]

    return SaleResponse(
        id=sale.id,
        store_id=sale.store_id,
        date=sale.date,
        total_amount=sale.total_amount,
        items=sale_items_responses,
    )


def get_sale(db: Session, sale_id: int):
    return db.query(Sale).filter(Sale.id == sale_id).first()


def update_sale(db: Session, sale_id: int, sale: SaleCreate):
    db_sale = get_sale(db=db, sale_id=sale_id)
    if db_sale:
        for key, value in sale.model_dump().items():  # Используем model_dump()
            setattr(db_sale, key, value)
        db.commit()
        db.refresh(db_sale)
    return db_sale


def delete_sale(db: Session, sale_id: int):
    db_sale = get_sale(db=db, sale_id=sale_id)
    if db_sale:
        db.delete(db_sale)
        db.commit()
    return db_sale


def get_all_sales(db: Session):
    return db.query(Sale).all()