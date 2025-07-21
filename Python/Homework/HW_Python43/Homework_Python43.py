"""Task 1. Добавление товаров
Создайте программу, которая подключается к MongoDB и:
выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
!!!очищает коллекцию перед началом!!!
добавляет 3 товара с полями: name, price, stock
выводит сообщение о количестве добавленных товаров
"""
print("Task 1. Добавление товаров, MongoDB")

from pymongo import MongoClient
try:
    mongo_client = MongoClient(
     "mongodb://ich_editor:verystrongpassword"
     "@mongo.itcareerhub.de/?readPreference=primary"
     "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
    )
    # connect to collection in MongoDB
    collection = mongo_client["ich_edit"]["products_210225_Platonova"]
except Exception as e:
    print("Connection error to BD:", e)
    exit()


# delete dos of collection
collection.delete_many({})

# add products:
products = [
    {"name": "Laptop", "price": 1000, "stock": 10},
    {"name": "Smartphone", "price": 800, "stock": 15},
    {"name": "Headphones", "price": 100, "stock": 5}
]

result = collection.insert_many(products)
print(f"{len(result.inserted_ids)} products inserted.")

"""Task 2. Увеличение цен на 20%
Продолжите предыдущую задачу. Теперь программа должна:
увеличить цену всех товаров на 20%
вывести количество обновлённых записей
затем вывести список всех товаров с новыми ценами
"""
print("\nTask 2. Увеличение цен на 20%")
#result = collection.update_many(
#    {},
#    {"$mul": {"price": 1.2}}
#    )
# print(f"Price updated for {result.modified_count} products.")
# result.modified_count -количество обновлённых записей


# variant with "round"
try:
    updated_counter = 0
    for doc in collection.find():
        old_price = doc.get("price", 0) # Если такого поля нет — верни 0 (ноль) вместо ошибки
        new_price = round(old_price * 1.2, 2)
        result = collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"price": new_price}}
        )
        updated_counter += result.modified_count
    print(f"Price updated for {updated_counter} products.")


    print("\nUpdated products:")
    for product in collection.find():       # collection.find() - all rows(doc) documents
        print(f"- {product['name']} - ${product['price']}")

except Exception as e:
    print("Update error:", e)