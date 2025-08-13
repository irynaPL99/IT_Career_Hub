''' Task 1. Число в конце
Напишите программу, которая создает новый список.
В него необходимо добавить только те строки из исходного списка,
в которых цифры находятся только в конце.
Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
'''

print("\n<<<<< Task 1.1 Число в конце >>>>>")
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
result = []
for item in strings:
    without_digits = item.rstrip('0123456789')  #убирает ВСЕ цифры с конца строки
    #print(item, without_digits)
    if without_digits.isalpha():      # Проверяем: вся оставшаяся часть — без цифр
        result.append(item)
    #    result+=(item,)
print(f"Строки с цифрами только в конце: {result}")
'''
print("\n<<<<< Task 1.2 Число в конце >>>>>")
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
result = []
result=[item for item in strings if item.rstrip('0123456789').isalpha()]
print(f"Строки с цифрами только в конце: {result}")
'''

'''Task 2. Удаление кратных
Напишите программу, которая удаляет из списка все значения, 
кратные числу, которое вводится пользователем.
Данные:
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
Пример вывода:
Введите число для удаления кратных ему элементов: 3
Список без кратных значений: [1, 10, 19, 20]
'''
print("\n<<<<< Task 2.1 Удаление кратных >>>>>")
numbers = [1, 3, 3, 6, 9, 10, 12, 15, 19, 20]
user_input=int(input("Введите число для удаления кратных ему элементов: "))
for item in numbers[:]:    # рабатаем с копией списка, чтобы не сдвигать индексы в реальном списке
    #print(item)
    if item % user_input == 0:
        numbers.remove(item)        # удаляем первое найденое вхождение из
print(f"Список без кратных значений:{numbers}")


'''Task 3. Порядок четных
Напишите программу, которая формирует !!новый!! список чисел. 
Добавьте в него все элементы исходного списка, где:
+нечетные числа занимают те же позиции,
+чётные числа отсортированы между собой обратном порядке.
Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]
'''
print("\n<<<<< Task 3.1 Порядок четных >>>>>")
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
output_numbers=[]
for item in numbers:                # обработка толька четных чисел
    if item % 2 == 0:
        output_numbers.append(item)
#print(f"только четные из output_numbers={output_numbers}")
output_numbers=sorted(output_numbers, reverse=True)
#print(f"sorted, четные из output_numbers={output_numbers}")

for idx,item in enumerate(numbers):                # обработка толька НЕчетных чисел
    if item % 2 != 0:
       #print(item)
       output_numbers.insert(idx,item)
       #print(f"+НЕчетные из output_numbers={output_numbers}")
print(f"Список после сортировки: {output_numbers}")
'''
print("\n<<<<< Task 3.2(AI) Порядок четных >>>>>")
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# Получаем отсортированные по убыванию чётные числа
even_sorted = sorted([n for n in numbers if n % 2 == 0], reverse=True)
# Подставляем чётные на места чётных, нечётные — сохраняем
output_numbers = []
even_idx = 0    # индексы для четных
for n in numbers:
    if n % 2 == 0:
        output_numbers.append(even_sorted[even_idx])
        even_idx += 1
    else:
        output_numbers.append(n)
print(f"Список после сортировки: {output_numbers}")
'''