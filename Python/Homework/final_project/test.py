
#test 1: invalid_mongo, Version: 4.13.2

#pip install pymongo==3.12.3
from pymongo import MongoClient
try:
    client = MongoClient("mongodb://ich_editor:verystrongpassword@invalid_mongo.itcareerhub.de")
    db = client["test"]
    print("Подключение успешно")
except Exception as e:
    print(f"Ошибка: {e}")