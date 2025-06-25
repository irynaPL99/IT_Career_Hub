'''Task 1. Создайте декоратор measure_time, который измеряет и
выводит среднее время выполнения функции за 5 вызовов.
Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.

'''
print("\nTask 1. Cреднее время выполнения функции за 5 вызовов. start...")
import time
from functools import wraps
#from time import sleep
from typing import Callable, Any

def measure_time(func: Callable) -> Callable:
    """Decorator to measure the average execution time of a function over 5 calls.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:    # может вернуть что угодно — строку, число, список, объект и т.д
        time_list = []
        result = None
        for _ in range(5):
            start_time = time.perf_counter() # возвращает текущее значение высокоточного таймера
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            time_list.append(end_time - start_time)
        avg_time = sum(time_list) / 5
        print(f"Cреднее время выполнения функции за 5 вызовов: {avg_time:.2f} секунд")
        print(f"Результат: {result}")
        return result
    return wrapper

@measure_time       # простой декоратор (не фабрика)
def compute():     # тестовая функция, для которой будет определяться замер времени вычислений
    #time.sleep(3)  # Имитация долгой операции
    total = 0
    for i in range(10_000_000):
        total += i
    return total

# main code
compute()


'''Task 2. Среднее время выполнения с количеством вызовов
Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.
'''
print("\nTask 2. Среднее время выполнения с количеством вызовов. Example: 10. Start...")
def measure_time(repeats: int) -> Callable:
    """
    Decorator that runs the function `repeats` times and prints average execution time.

    :param repeats: number of times the function will be executed
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            time_list = []
            result = None
            for _ in range(repeats):
                #print(_)
                start_time = time.perf_counter() # возвращает текущее значение высокоточного таймера
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                time_list.append(end_time - start_time)
            avg_time = sum(time_list) / repeats
            print(f"Cреднее время выполнения функции за {repeats} вызовов: {avg_time:.2f} секунд")
            print(f"Результат: {result}")
            return result
        return wrapper
    return decorator


@measure_time(10) #  кол-во вызовов; фабрика-декоратор
def compute():
    total = 0
    for i in range(10_000_000):
        total += i

    return total

# main code
compute()
