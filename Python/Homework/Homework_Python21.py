'''Task 1. Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь
с подсчётом количества каждой буквы, игнорируя регистр.
Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
'''
print("\n <<<<< Task 1.0 Повторения букв  >>>>>")
from collections import Counter
def check_count_char(string):
    # Приводим текст к нижнему регистру и фильтруем только буквы
    filtered = [char.lower() for char in string if char.isalpha()]
    # print(filtered)
    # print(Counter(filtered))
    return dict(Counter(filtered))  # Преобразуем Counter в обычный словарь

text = "Programming is fun!"
print(check_count_char(text))

print("\n <<<<< Task 1.1 Повторения букв  >>>>>")
def check_count_char(string):
    dict_char = {}
    for char in string.lower():
        if char.isalpha() and char not in dict_char:
            dict_char[char] = string.lower().count(char)
    return dict_char

text = "Programming is fun!"
print(check_count_char(text))

print("\n <<<<< Task 1.2 Повторения букв  >>>>>")
def check_count_char(string):
    dict_char = {}
    for char in string.lower():
        if char.isalpha():
            if char in dict_char:
                dict_char[char] += 1
            else:
                dict_char [char] = 1
    return dict_char

text = "Programming is fun!"
print(check_count_char(text))

'''Task 2. Группировка студентов по классам
Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
'''
print("\n <<<<< Task 2.0 Группировка студентов по классам  >>>>>")
from collections import defaultdict

def sort_students(students):
    group_class = defaultdict(list)
# defaultdict(list) - автоматически создавать списки (или другие типы контейнеров) по ключам, не проверяя каждый раз наличие ключа
    for class_num, name in students:
        group_class[class_num].append(name)
    return dict(group_class)  # преобразуем defaultdict в обычный словарь для вывода

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
print(sort_students(students))

print("\n <<<<< Task 2.1 Группировка студентов по классам  >>>>>")
def sort_students(students):
    group_class = {}
    for class_num, name in students:
        if class_num not in group_class:
            group_class[class_num] = [name]
        else:
            group_class[class_num].append(name)
    return group_class

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
print(sort_students(students))


print("\n <<<<< Task 2.2 Группировка студентов по классам  >>>>>")
def sort_students(students):
    group_class = {}
    for class_num, name in students:
# dict.setdefault() — позволяет избежать явной проверки "if key not in dict:"
        group_class.setdefault(class_num,[]).append(name)
    return group_class

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
print(sort_students(students))