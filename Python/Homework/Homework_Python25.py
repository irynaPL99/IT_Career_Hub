'''Task 1. Деление без ошибок
Напишите функцию, которая выполняет деление двух чисел, введенных пользователем,
и обрабатывает возможные ошибки.
Пример вывода:
Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.

print("\nTask 1. Деление без ошибок")
def fun_division(a: float, b: float) -> float:
    try:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = a / b
        print(f"Результат: {result}")
        return result

    except ValueError:
        print("Ошибка: Введено некорректное число.")
        return None

    except ZeroDivisionError as e:
        print(f"Ошибка:{e}")

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    fun_division(a,b)

except ValueError:
    print("Ошибка: Введено некорректное число.")
'''
'''Task 2. Логирование ошибок
Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии 
с форматом ниже.
Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.
'''
print("\nTask 2. Логирование ошибок")
import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - ERROR - %(filename)s - %(lineno)d - %(message)s', encoding='utf-8'
)
def fun_division(a: float, b: float) -> float:
    try:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = a / b
        print(f"Результат: {result}")
        return result

    except ValueError:
        logging.error("Ошибка: Введено некорректное число")
        print("Ошибка: Введено некорректное число")
        #return None
        # добавление явного return None  показываем,
        # что в случае ошибки функция намеренно возвращает None
        # (это сигнализирует, что деление не удалось из-за ошибки.).

    except ZeroDivisionError as e:
        logging.error(f"Ошибка: {e}")
        print(f"Ошибка: {e}")
        #return None

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    fun_division(a, b)

except ValueError:
    logging.error("Ошибка: Введено некорректное число")
    print("Ошибка: Введено некорректное число")