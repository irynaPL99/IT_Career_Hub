'''Task 1. Реверс словаря
Напишите программу, которая меняет местами ключи и значения в словаре.
Если значения повторяются, добавьте их в список.
Данные:
data = {"a": 1, "b": 2, "c": 1, "d": 3}
Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
'''
print("\n<<<<<Task 1.1 Реверс словаря >>>>>")
data = {"a": 1, "b": 2, "c": 1, "d": 3}
output_data = {}
for key, value in data.items():
    #print(key,value)
    if value in output_data: # wie key
        output_data[value].append(key) # hinzufügen neue value
    else:
        output_data[value] = [key] # wie list
print("Перевернутый словарь:", output_data)

print("\n<<<<<Task 1.2 Реверс словаря >>>>>")
data = {"a": 1, "b": 2, "c": 1, "d": 3}
output_data = {}
for key, value in data.items():
    # setdefault(value, []) — если value ещё нет в output_data, создаёт новую запись со значением [].
    # .append(key) — сразу добавляет текущий ключ.
    output_data.setdefault(value,[]).append(key) # value wie key, key wie value
print("Перевернутый словарь:", output_data)


'''Task 2. Счётчик букв в словах
Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и 
создаёт словарь, где ключи — это слова, а значения — это ещё один словарь 
с подсчётом каждой буквы.
Данные:
words = ["anna", "bennet", "john"]
Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}
'''
print("\n<<<<<Task 2.1 Счётчик букв в словах >>>>>")
words = ["anna", "bennet", "john"]
output_words = {}
for word in words:
    cnt = 0
    char_dict = {}      # создаём новый словарь для каждого слова
    for char in word:
        if char not in char_dict:
            cnt = word.count(char)
            #print(char, cnt)
            char_dict[char] = cnt
            #print(char_dict)
        else:
            pass
        output_words[word] = char_dict
print(output_words)


print("\n<<<<<Task 2.2 Счётчик букв в словах >>>>>")
words = ["anna", "bennet", "john"]
output_words = {}
for word in words:
    char_dict = {}
    for char in word:
        char_dict[char] = char_dict.get(char, 0) + 1
        # текущее значение по ключу char.
        # Если ключа ещё нет, возвращает 0. Наращиваем на 1
    output_words[word] = char_dict
print(output_words)


'''Task 3. Распределение студентов по группам
У вас есть словарь, где ключи — имена студентов, а значения — их баллы за экзамен.
Необходимо распределить студентов по группам:
"Отличники": баллы >= 85
"Хорошисты": баллы от 70 до 84
"Троечники": баллы от 50 до 69
"Не сдали": баллы < 50
Создайте словарь с ключами-группами и словарями со студентами в качестве значений.
Данные:
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
Пример вывода:
Распределение по группам:
{'Отличники': {'Аня': 92, 'Дима': 88}, 'Хорошисты': {'Боря': 76}, 
'Троечники': {'Ваня': 65, 'Ева': 54}, 'Не сдали': {'Галя': 48}}
'''
print("\n<<<<<Task 3.1 Распределение студентов по группам >>>>>")
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
# Создаём отдельный пустой словарь для каждой группы
output_groups = {group: {} for group in groups}
for name, grade in students.items():
    if grade >= 85:
        output_groups["Отличники"][name] = grade
    elif grade >= 70:
        output_groups["Хорошисты"][name] = grade
    elif grade >= 50:
        output_groups["Троечники"][name] = grade
    else:
        output_groups["Не сдали"][name] = grade

print("Распределение по группам:", output_groups)


print("\n<<<<<Task 3.2 Распределение студентов по группам >>>>>")
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
# Создаём отдельный пустой словарь для каждой группы
output_groups = {group: {} for group in groups}
for name, grade in students.items():
    match grade:
        case grade if grade >= 85:
            output_groups["Отличники"][name] = grade
        case grade if grade >= 70:
            output_groups["Хорошисты"][name] = grade
        case grade if grade >= 50:
            output_groups["Троечники"][name] = grade
        case _:
            output_groups["Не сдали"][name] = grade
print("Распределение по группам:", output_groups)