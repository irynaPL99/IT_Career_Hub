'''Task 1. Одно слово
Напишите программу, которая обрабатывает список из строк и
удаляет все строки, содержащие более одного слова,
а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
'''
print("\n<<<<< Task 1.1 Одно слово  >>>>>")
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
new_list=[]
for text in text_list:
    if text.count(" ")==0:
        #print(text)
        new_list.append(text.lower())
print(f"Обработанный список: {new_list}")

'''
print("\n<<<<< Task 1.2(AI) Одно слово  >>>>>")
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
text_list = [text.lower() for text in text_list if text.count(" ")==0]
print(f"Обработанный список: {text_list}")
'''

'''Task 2. Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару 
и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17
Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse               25.00$        20.75$
Keyboard            75.00$        62.25$
Monitor            200.00$       166.00$
'''
print("\n<<<<< Task 2.1 Обновление цен товаров  >>>>>")
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount=float(input("Введите скидку (в процентах):"))
print(f"{'Товар':15}{'Старая цена':>11}{'Новая цена':>14}")
for product,price in products:
    new_price=price*(1-discount/100)
    new_price=f"{new_price:.2f}$"
    price=f"{price:.2f}$"
    print(f"{product:15}{price:>11}{new_price:>14}")

'''
print("\n<<<<< Task 2.2(AI) Обновление цен товаров  >>>>>")
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount=float(input("Введите скидку (в процентах):"))
print(f"{'Товар':15}{'Старая цена':>12}{'Новая цена':>15}")
for product,price in products:
    print(f"{product:15}{price:>11.2f}${price*(1-discount/100):>14.2f}$")
'''