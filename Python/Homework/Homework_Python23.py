'''Task 1. Объединение данных в строку
Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари)
и возвращает их строковое представление, объединённое через " | ".
Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
Пример вывода:
42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
'''
print("\nTask 1. Объединение данных в строку")
from typing import List, Any
# List[Any] — The function accepts a list of any types of data
def join_text (data: List[Any]) -> str:
    """
    Join elements of a list into a single string separeted by ' | ',
    converting euch element to a string.

    :param data: A list containing any type of data (numbers, strings,
     lists, dictonaries, etc.)
    :return: A string with all elements joined using ' | '
    """
    return " | ".join(str(item)  for item in data)

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
print(join_text(data))

'''Task 2. Сумма вложенных чисел
Напишите функцию, которая принимает список словарей, где каждый словарь 
содержит имя пользователя и список баллов. Функция должна вернуть сумму всех чисел. 
Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
Данные:
data = [ {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}]
Пример вывода:
Итоговый балл: 156
'''
print("\nTask 2. Сумма вложенных чисел")
from typing import List, Dict
def total_sum(data: List[Dict[str, List[int]]]) -> int:
    """
    Calculates the total sum of all scores from a list of user dictionaries.
    Each dictionary should contain a 'name' (string) and a score list (list of integers).
    :param data:  List of dictionaries with user names and their list of scores.
    :return: The total sum of all scores from all users.
    """
    return sum(score for user in data for score in user["scores"])

data = [ {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]} ]
print(total_sum(data))
