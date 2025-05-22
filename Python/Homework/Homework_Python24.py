'''recursion. Task *. Задача "флэттенинга" (flatten) — развертывания вложенных списков с помощью рекурсии.
[[[[[2, [[[[3, [[[[4, [[[[[5]]]]]]]]]]]]]]]]]] -> [2, 3, 4, 5]
'''
print("\nTask *. Задача \"флэттенинга\" (flatten)")
from typing import Any, List

def flatten(nested_list: list[Any]) -> List[Any]:
    """
    Turn a nested list into a flat (one-level) list.
    :param nested_list: A list that may contain other lists.
    :return: list: A flat list with all elements from the nested list in order.
    Example:
            >>> flatten([1, [2, 3], 4])
            [1, 2, 3, 4]
            >>> flatten([1, [2, [3, 4], 5]])
            [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):          # проверяет, является ли текущий item списком
            # extend добавляет каждый элемент списка по отдельности.
            result.extend(flatten(item))  # рекурсивно разворачиваем вложенный список
        else:
            result.append(item)           # если не список, просто добавляем
    return result

nested_list = [[[[[2, [[[[3, [[[[4, [[[[[5]]]]]]]]]]]]]]]]]]
print(flatten(nested_list))     # ➜ [2, 3, 4, 5]

'''HW24 Task 1. Сумма цифр числа
Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
Данные:
num = 43197
Пример вывода:
24
'''
print("\nTask 1. Сумма цифр числа")
def sum_digits(num: int) -> int:
    """
    Find the sum of all digits in a number using recursion.
    :param num (int): A number to sum its digits.
    :return (int): The sum of all digits in the number.
    Example:
        >>> sum_digits(43197)
        24
        >>> sum_digits(123)
        6
    """
    # If number is negative, make it positive
    num = abs(num)
    # Base case: if number is less than 10, it has one digit, return it
    if num < 10:
        return num
    # Recursive case: take last digit (num % 10) and add to sum of other digits
    return (num % 10) + sum_digits(num // 10)

num = 43197
print(sum_digits(num))

'''Task 2. Сумма вложенных чисел
Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
'''
print("\nTask 2. Сумма вложенных чисел")
from typing import Any, List

def flatten_sum(nested_numbers: list[Any]) -> int:
    """
    Sum all numbers in a nested list using recursion.
    :param nested_numbers (list): A list that may contain numbers or other lists.
    :return (int): The sum of all numbers in the nested list.
    """
    total_sum = 0
    for item in nested_numbers:
        #print(f"Processing item: {item}")
        if isinstance(item, list):
            #  If item is a list, call the function !!again!! and add the result to total
            #total_sum += flatten_sum(item)
            sub_sum = flatten_sum(item)
            #print(f"Adding sub_sum from list {item}: {sub_sum}")
            total_sum += sub_sum
        else:
            total_sum += item  #
    return total_sum

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
#print("Input list:", nested_numbers)
print(flatten_sum(nested_numbers))