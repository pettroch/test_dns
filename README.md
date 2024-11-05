# Запуск приложения
Запустить файл app.py, который находится в папке /src

Сначала добавить город, потом магазин, потом продукт по соответствующим роутам

# Как использовать API
## Products
### **GET /products** - получение всех продуктов
Ответ:
```
[
  {
    "id": int - айди продукта,
    "name": str - название,
    "price": float - цена
  }
]
```

### **POST /products** - создание продукта
Пример:
```
{
  "name": str - название продукта,
  "price": float - цена,
  "store_id": id - айди магазина
}
```
Ответ:
```
{
  "id": int,
  "name": str,
  "price": float
}
```

### **GET /products/{product_id}** - получение продукта по айди
Пример:
```
param: product_id: int - айди продукта
```
Ответ:
```
{
  "id": int - айди продукта,
  "name": str - название продукта,
  "price": float - цена
}
```

### **PUT /products/{product_id}** - обновление продукта по айди
Пример:
```
param: product_id: int - айди продукта

{
  "name": str - название продукта, 
  "price": float - цена продукта,
  "store_id": int - айди магазина
}
```
Ответ:
```
{
  "id": int - айди продукта,
  "name": str - название продукта,
  "price": float - цена
}
```

### **DELETE /products/{product_id}** - удаление продукта по айди
Пример:
```
param: product_id: int - айди продукта
```
Ответ:
```
{
  "id": int - айди продукта,
  "name": str - название продукта,
  "price": float - цена
}
```


## Cities
### **GET /cities** - получение всех городов
Ответ:
```
[
  {
    "id": int - айди города,
    "name": str - название города
  }
]
```

### **POST /cities** - добавление города
Пример:
```
{
  "name": str - название города
}
```
Ответ:
```
{
  "id": int - айди города,
  "name": str - название города
}
```

### **GET /cities/{city_id}** - получение города по айди
Пример:
```
param: city_id: int - айди города
```
Ответ:
```
{
  "id": int - айди города,
  "name": str - название города
}
```

### **PUT /cities/{city_id}** - обнолвние названия города
Пример:
```
param: city_id: int - айди города

{
  "name": str - название города
}
```
Ответ:
```
{
  "id": int - айди города,
  "name": str - название города
}
```

### **DELETE /cities/{city_id}** - удаление города
Пример:
```
param: city_id: int - айди города
```
Ответ:
```
{
  "id": int - айди города,
  "name": str - название города
}
```

## Stores
### **GET /stores** - получение всех магазинов
Ответ:
```
 [
  {
    "id": int - айди магазина,
    "name": str - название магазина,
    "city_id": int - айди города
  }
]
```

### **POST /stores** - добавление магазина
Пример:
```
{
  "name": str - название магазина,
  "city_id": int - айди города
}
```
Ответ:
```
{
  "id": int - айди магазина,
  "name": str - название магазина,
  "city_id": int - айди города
}
```

### **GET /stores/{store_id}** - получение магазина по айди
Пример:
```
param: store_id: int - айди магазига
```
Ответ:
```
{
  "id": int - айди магазина,
  "name": str - название магазина,
  "city_id": int - айди города
}
```

### **PUT /stores/{store_id}** - обновление магазина
Пример:
```
param: store_id: int - айди магазина

{
  "name": str - название магазина,
  "city_id": int - айди города
}
```
Ответ:
```
{
  "id": int - айди магазина,
  "name": str - название магазина,
  "city_id": int - айди города
}
```

### **DELETE /stores/{store_id}** - удаление магазина
Пример:
```
param: store_id: int - айди магазина
```
Ответ:
```
{
  "id": int - айди магазина,
  "name": str - название магазина,
  "city_id": int - айди города
}
```

## Sales
### **GET /sales** - получение всех продаж
Ответ:
```
[
  {
    "id": int - айди продажи,
    "store_id": int - айди магазина,
    "date": str - дата продажи,
    "total_amount": float - общее кол-во,
    "items": [
      {
        "product_id": int - айди продукта,
        "quantity": int - кол-во,
        "price": float - цена,
        "total_price": float - общая цена,
        "id": int - айди конкретной продажи
      }
    ]
  }
]
```

### **POST /sales** - создание продажи
Пример:
```
[
  {
    "id": int - айди продажи,
    "store_id": int - айди магазина,
    "date": str - дата продажи,
    "total_amount": float - общее кол-во,
    "items": [
      {
        "product_id": int - айди продукта,
        "quantity": int - кол-во,
        "price": float - цена,
        "total_price": float - общая цена,
        "id": int - айди конкретной продажи
      }
    ]
  }
]
```
Ответ:
```
{
    "id": int - айди продажи,
    "store_id": int - айди магазина,
    "date": str - дата продажи,
    "total_amount": float - общее кол-во,
    "items": [
        {
            "product_id": int - айди продукта,
            "quantity": int - кол-во,
            "price": float - цена,
            "total_price": float - общая цена,
            "id": int - айди конкретной продажи
        }
    ]
}
```

### **GET /sales/city/{city_id}** - получение продаж по городу
Пример:
```
param: city_id: int - айди города
```
Ответ:
```
[
  {
    "id": int - айди продажи,
    "store_id": int - айди магазина,
    "date": str - дата продажи,
    "total_amount": float - общее кол-во,
    "items": [
      {
        "product_id": int - айди продукта,
        "quantity": int - кол-во,
        "price": float - цена,
        "total_price": float - общая цена,
        "id": int - айди конкретной продажи
      }
    ]
  }
]
```

### **GET /sales/store/{store_id}** - получение продаж по магазину
Пример:
```
param: store_id: int - айди магазина
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/product/{product_id}** - получение продаж по продукту
Пример:
```
param: product_id: int - айди продукта
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/last_days** - получение продаж за n дней
Пример:
```
param: n_days: int - кол-во дней
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/above/{n_amount}** - получение продаж больше n суммы
Пример:
```
param: n_amount: int - сумма
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/below/{n_amount}** - получение продаж меньше n суммы
Пример:
```
param: n_amount: int - сумма
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/quantity_above/{n_quantity}** - получение продаж больше n кол-ва
Пример:
```
param: n_quantity: int - кол-во
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/quantity_below/{n_quantity}** - получение продаж меньше n кол-ва
Пример:
```
param: n_quantity: int - кол-во
```
Ответ:
```
[
  {
    "product_id": int - айди продукта,
    "quantity": int - кол-во,
    "price": float - цена,
    "total_price": float - общая сумма,
    "id": id - айди продажи
  }
]
```

### **GET /sales/{sale_id}** - получение продажи по айди
Пример:
```
param: sale_id: int - айди продажи
```
Ответ:
```
{
    "id": int - айди продажи,
    "store_id": int - айди магазина,
    "date": str - дата продажи,
    "total_amount": float - общее кол-во,
    "items": [
        {
            "product_id": int - айди продукта,
            "quantity": int - кол-во,
            "price": float - цена,
            "total_price": float - общая цена,
            "id": int - айди конкретной продажи
        }
    ]
}
```

### **PUT /sales/{sale_id}** - обновление продажи
Пример:
```
param: sale_id: int - айди продажи

{
  "store_id": int - айди магазина,
  "date": str - дата,
  "total_amount": float - сумма,
  "items": [
    {
      "product_id": int - айди продукта,
      "quantity": int - кол-во,
      "price": float - цена,
      "total_price": float - сумма
    }
  ]
}
```

### **DELETE /sales/{sale_id}** - удаление продажи
Пример:
```
param: sale_id: int - айди продажи
```
Ответ:
```
{
  "id": int - айди
  "store_id": int - айди магазина,
  "date": str - дата,
  "total_amount": float - сумма,
  "items": [
    {
      "product_id": int - айди продукта,
      "quantity": int - кол-во,
      "price": float - цена,
      "total_price": float - сумма
      "id": int - айди
    }
  ]
}
```

#### Документация доступна по http://127.0.0.1:5000/docs