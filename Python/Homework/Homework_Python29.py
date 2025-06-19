'''Task 1. Генератор Фибоначчи
Создайте генератор, который генерирует последовательность Фибоначчи бесконечно,
возвращая по одному числу за раз.
Последовательность Фибоначчи — это ряд чисел, где каждое следующее число
равно сумме двух предыдущих.
Начинается с 0 и 1.
Пример вывода:
0
1
1
2
3
5
8
13
21
34
'''
print("\nTask 1. Генератор Фибоначчи ")
from typing import Generator
def gen_fibonacci() -> 'Generator[int, None, None]':
    """
    Infinite generator for Fibonacci numbers.
    Yields one Fibonacci number at a time.
    """
    x ,y = 0, 1
    while True:
        yield x
        x , y = y, (x+y)

# main code
gen = gen_fibonacci()
for _ in range(10):
    print(next(gen))

'''Task 2. Генератор уникальных элементов
Создайте генератор, который принимает список элементов и 
выдаёт только уникальные значения,
сохраняя порядок их появления в исходном списке.
Данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
Пример вывода:
3
1
2
4
5
6
7
8
'''
print("\nTask 2. Генератор уникальных элементов")
from typing import Generator
def gen_uniq_item(data: list[int]) -> 'Generetor(int, None, None)':
    """
    Generator that yields only unique elements from the input list,
    preserving the order of their first appearance.

    :param data: List of input elements.
    :return: Generator of unique elements.
    """
    seen_items = set() # set -множество не допускает дубликаты и оно быстрое для поиска
    for item in data:
        if item not in seen_items:
            seen_items.add(item)
            yield item

# main cod
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
for _ in gen_uniq_item(data):
    print (_)