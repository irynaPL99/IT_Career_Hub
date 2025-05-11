'''Task 1 Простое число
Напишите функцию, которая проверяет, является ли число n простым
(делится только на 1 и само себя) и возвращает булевый результат.
Данные:
n = 17
Пример вывода:
Число 17 является простым
'''
print("\n <<<<< Task 1. Простое число  >>>>>")
def check_value(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1): #range не включает верхнюю границу
        # если число делится на что.то, то оно обязательно делиться на число в диапозоне
        # до квадратного корня от числа. Можно сократить кол-во проверок
        # n**0.5 — возведение числа n в степень 0.5 (квадратный корень)
        if n % i == 0:
            return False
        else:
            return True
#n=int(input("n="))
n = 17
if check_value(n):
    print(f"Число {n} является простым")
else:
    print(f"Число {n} не является простым")


'''Task 2 Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd") и 
произвольное количество чисел, возвращая только те, которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
'''
print("\n <<<<< Task 2. Фильтрация чисел по чётности  >>>>>")
def filter_numbers(filter_type, *args):
    if filter_type == "even":
        return [n for n in args if n % 2 == 0]
    elif filter_type == "odd":
        return [n for n in args if n % 2 != 0]
    else:
        return "Некорректный фильтр"

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))


'''Task 3 Объединение словарей
Напишите функцию, которая принимает !! любое !!! количество словарей и объединяет их в один. 
Если ключи повторяются, используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
Пример вызова:
print(merge_dicts(dict1, dict2, dict3))
Пример вывода:
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
'''
print("\n <<<<< Task 3.1 Объединение словарей  >>>>>")
def merge_dicts(*dicts): # *dicts позволяет передать любое количество словарей как позиционные аргументы
    # Если одни и те же ключи встречаются в нескольких словарях, берётся значение из последнего.
    output_dict = {}
    for d in dicts:
        #v1 output_dict.update(d)  # добавляет все пары ключ–значение
        #v2 output_dict |= d  # оператор объединения словарей
        output_dict |= d
    return output_dict
    # Метод update() добавляет все пары ключ–значение из d в output_dict.
    #  Если ключ уже существует — его значение заменяется.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
print(merge_dicts(dict1, dict2, dict3))


print("\n <<<<< Task 3.2 Объединение словарей  >>>>>")
def merge_dicts(*dicts): # *dicts позволяет передать любое количество словарей как позиционные аргументы
    # Если одни и те же ключи встречаются в нескольких словарях, берётся значение из последнего.
    output_dict = {}
    for d in dicts:
        for key,value in d.items():
            output_dict[key] = value
    return output_dict
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
print(merge_dicts(dict1, dict2, dict3))