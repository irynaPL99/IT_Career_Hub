'''Task 1. Фабрика функций округления
Создайте функцию make_rounder(), которая принимает количество знаков
для округления и возвращает другую функцию.
Полученная функция должна принимать число и возвращать его,
округлённое до указанного ранее количества знаков после запятой.
Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))
Пример вывода:
3.14
2.72
10.0'''
print("\nTask 1. Фабрика функций округления")
def make_rounder(digits: int) -> callable:
    """
    This function makes and returns another function.
    The returned function will round a number to 'digits' decimal places.

    :param digits: Number of decimal places (for example, 2)
    :return: A function that takes a number and returns a rounded number
    """
    def round_number(n: float) -> float:
        """
        Round the input number to 'digits' decimal places.

        :param n: Any number (like 3.1415)
        :return: Rounded number (like 3.14)
        """
        return round(n, digits)
    return round_number

# main code
round2 = make_rounder(2) #-> create function to round 2 digits
round0 = make_rounder(2) #-> create function to round 0 digits
#round1 = make_rounder(1)
print(round2(3.14159)) #3.14
print(round2(2.71828)) #2.72
print(round0(9.999))  #10.0
#print(round1(9.999)) #10.0


'''Task 2. Расширяемый логгер событий
Создайте функцию, которая возвращает вложенный логгер событий.
Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано) и
возвращать весь список событий.
Пример вызова: 
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)
Пример вывода: 
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29
#!!! Рамка вокруг вывода !!!
#Создайте декоратор frame,
'''
print("\nTask 2. Расширяемый логгер событий")
from datetime import datetime
from typing import List, Callable
#from functools import wraps

# decorator "frame"
#def frame(func: Callable) -> Callable:
#@wraps(func)    # чтобы сохранить метаданные функции function "func_make_loge
#def wrapper(*args, **kwargs):
#    border = "=" * 42
#    print(border)
#    result_list_events = func(*args, **kwargs) # call the function "func_make_loger"
#    for text in result_list_events:
#        print(text)
#    print(border)
#    return result_list_events
#return wrapper

def func_make_loger() -> Callable[[str], List [str]]:
    """
    This function makes a logger.
    The logger remembers all messages.
    Each message has the current time.

    :return: a function that adds or shows event.
    """
    list_messages = [] # List[str] - a list to store all messages

    def log(event_text: str = "") -> List[str]:
    # event_text - строка, по умолчанию может быть пустой
        """
        This is the real logger function.
        If we give a message, it saves it with the current time.
        If we give NO message, it shows all saved messages.
        :param event_text: the message text
        :return: list of all messages
        """
        if event_text:
            now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            list_messages.append(f"{event_text}: {now_time}") # add message to list
        return list_messages # return  all saved messages
    return log # give back the Logger function

#  main code
log = func_make_loger() # собирает события
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)

# Оборачиваем вывод в рамку
#@frame
#def print_list_events(): # функция, возвращающая список событий
#    return log()

#print_list_events() # печать лога

'''Task 3. Рамка вокруг вывода
Создайте декоратор frame, который оборачивает результат функции
рамкой из 50 символов -, выводя по строке до и после вызова функции.
Пример декорируемой функции: 
def say_hello():
    print("Привет, игрок!")
Пример вывода: 
--------------------------------------------------
Привет, игрок!
--------------------------------------------------
'''
print("\nTask 3.  Рамка вокруг вывода")
from functools import wraps
from typing import Callable

# decorator
def frame(func: Callable) -> Callable:
    """Decorator that adds a frame of 50 dashes before and after function output."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        border = "-" * 50
        print(border)
        result = func(*args, **kwargs)
        print(border)
        return result
    return wrapper

@frame
# @frame(symbol="*", length=40)
def say_hello():
    print("Привет, игрок!")

# main code
say_hello()