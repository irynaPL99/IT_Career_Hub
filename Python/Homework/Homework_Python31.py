'''Task 1. Извлечение дат
Реализуйте программу, которая должна:
Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
'''
print("\nTask 1. Извлечение дат")
import re
from typing import Generator

def find_pattern_date(text: str) -> Generator[str, None, None]:
    """
    Generator that yields all dates in formats DD/MM/YYYY, DD-MM-YYYY, or DD.MM.YYYY.

    :param text: Input text containing dates
    :return: A date string
    """
    pattern = r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'
    for match in re.finditer(pattern, text):
    # re.finditer - Эта функция ищет все совпадения регулярного выражения в строке и возвращает итератор объектов Match
        #print("Yielding date:", match.group()) # match.group()- Полное совпадение
        yield match.group()


# \b — граница слова (чтобы не захватывать числа внутри слов).
# '\d{2} — две цифры (день и месяц).
# [-/.] — один из символов -, / или . (разделители дат).
# \d{4} — четыре цифры (год).
# re.finditer - для поиска всех дат по шаблону


# main code
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
for _ in find_pattern_date(text):
    print(_)


'''Task 2. Разделение списка тегов
Реализуйте программу, которая должна:
Прочитать строку с тегами, введёнными пользователем.
Разделить её на отдельные теги, независимо от того, 
чем они были разделены (запятые, точки с запятой, слэши или пробелы).
Удалить лишние пробелы и пустые значения.

text_input = "python, data-science / machine-learning; AI neural-networks"

print("\n Task 2.1 Разделение списка тегов")
import re
text_input = "python ,  data-science / machine-learning; AI neural-networks"
text_list = re.split(r'[\s,;/]+', text_input) #->list
# разбивает строку по любым символам-разделителям: , ; / и пробел (\s)
# + означает "один или более", т.е. несколько подряд не вызовут пустых элементов
#print("text_list:", text_list)
print(text_list)
# Удаляем пустые строки и пробелы
#text_clean = [item.strip() for item in text_list if item.strip()]
#if item.strip() — отбрасывает пустые элементы.
#print("text_clean:", text_clean)
'''
print("\n Task 2.2 Разделение списка тегов (with def)")
import re

def find_tags(text_input: str) -> list:
    text_list = re.split(r'[\s,;/]+', text_input)
    return text_list
# main code
text_input = "python ,  data-science / machine-learning; AI neural-networks"
print (find_tags(text_input))