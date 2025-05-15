'''Task 1. Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.
Данные:
orders = [{"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400} ]
Пример вывода:
['Chair', 'Laptop']
'''
from itertools import product

print("\n Task 1.1  Выбор заказов")
def filter_orders(order_list,key_product,key_price,max_price):
    result=[]
    for product in order_list:      # for item in order_list
        if product[key_price] > 500:
            result += [product[key_product]]
    return sorted(result)

orders = [{"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400} ]

print(filter_orders(orders,"product","price",500))

print("\n Task 1.2 mit list comprehension,  Выбор заказов")
def filter_orders0(order_list0):
    return sorted([product["product"] for product in order_list0 if  product["price"] > 500])

orders = [{"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400} ]
print(filter_orders0(orders))

print("\n Task 1.3 mit lambda/filter/map,  Выбор заказов")
def filter_orders1(order_list1):
    #filtered_orders = filter (lambda product: product.get("price",0) > 500, order_list1)
    filtered_orders = filter(lambda product: product["price"] > 500, order_list1)
    result_list = map(lambda product: product["product"], filtered_orders)
    return sorted(result_list)

orders = [{"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400} ]
print(filter_orders1(orders))


print("\n Task 1.4 mit collections.defaultdict,  Выбор заказов")
from collections import defaultdict
def filter_orders2(order_list2):
    result2 = defaultdict(list) #если по ключу ещё нет значения, создаём пустой список
    for product in order_list2:
        if product["price"] > 500:
            result2[product["price"]].append(product["product"])
            result2_output = sorted(result2.values())
    # return print(*result2_output)
    return [item for sublist in result2_output for item in sublist ]
orders = [{"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400} ]
#print(f"filter_orders2:{filter_orders2(orders)}")
print(filter_orders2(orders))

print("\n Task 1.5 mit functools.reduce,  Выбор заказов")
from functools import reduce
def filter_orders3(order_list3):
    result3 = reduce(
        lambda result3_list, product: result3_list + [product["product"]] if product["price"] > 500
        else result3_list, order_list3,
        []
    )
    return sorted(result3)

orders = [{"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400} ]
print(filter_orders3(orders))

''' Task 2. Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:
Вычисляет общую выручку для каждого товара.
Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
Данные:
sales = [("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)]
Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
'''
print("\n Task 2.1 Статистика продаж")
def statistic(products_list):
    result = {}
    for name, quantity, price in products_list:
        result[name] = quantity * price
        #result[name] = result.get(name,0) + quantity * price
    sorted_result = dict(sorted(result.items(), key = lambda product: product[1], reverse = True))
    return sorted_result

sales = [("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)]

print(statistic(sales))

print("\n Task 2.2 mit dict comprehation, Статистика продаж")
def statistic_1(products_list1):
    result = {name : quantity * price for name, quantity, price in products_list1  }
    return  dict(sorted(result.items(), key = lambda product: product[1], reverse = True))

sales = [("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)]

print(statistic_1(sales))


print("\n Task 2.3 mit map and lambda, Статистика продаж")
def statistic_2(products_list2):
    # Преобразуем кортежи в пары (товар, выручка)
    result_2 = map(lambda product: (product[0], product[1] * product [2]), products_list2)
    return dict(sorted(result_2, key = lambda x : x[1], reverse = True))

sales = [("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)]

print(statistic_2(sales))

print("\n Task 2.4 mit Counter, Статистика продаж")
from collections import Counter
def statistic_3(products_list3):
    result_3 = Counter()
    for name, quantity, prise in products_list3:
        result_3[name] = quantity * prise
    return dict(sorted(result_3.items(), key = lambda x: x[1], reverse = True))

sales = [("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)]

print(statistic_3(sales))