''' Task 1. Прогрессия увеличения
Напишите программу, которая создаёт новый кортеж,
состоящий из элементов изначального в том же порядке.
Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
Данные:
numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)

print("\n<<<<< Task 1.1 Прогрессия увеличения >>>>> ")
numbers = (3, 7, 2, 8, 5, 10, 1)
numbers_new=()
for index, value in enumerate(numbers):
    #print(index, value)
    if value > numbers[index-1]:
        numbers_new+=(value,)
print(f"Кортеж по возрастанию:{numbers_new}")
'''
'''
print("\n<<<<< Task 1.2 Прогрессия увеличения >>>>> ")
numbers = (3, 7, 2, 8, 5, 10, 1)
#print(len(numbers))
numbers_new =[numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        numbers_new.append(numbers[i])
#numbers_new = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
numbers_new = tuple(numbers_new)
print(f"Кортеж по возрастанию:{numbers_new}")
'''
print("\n<<<<< Task 1.3 Прогрессия увеличения >>>>> ")
numbers = (3, 7, 2, 8, 5, 10, 1)
print("Данные:",numbers)
numbers_new =[]
numbers_new = [numbers[i] for i in range(0, len(numbers)) if numbers[i] > numbers[i - 1]]
numbers_new = tuple(numbers_new)
print(f"Кортеж по возрастанию:{numbers_new}")

''' Task 2. Повторяющиеся элементы
Напишите программу, которая находит индексы элементов кортежа, 
встречающихся !!!более одного раза!!!. 
Вывести сами элементы и их индексы.
Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9 
Индексы элемента 3: 2 6 
Индексы элемента 4: 3 8

print("\n<<<<< Task 2.1 Повторяющиеся элементы >>>>> ")
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
numbers_list=()
for value in numbers:
    indexes = ()
    if value not in numbers_list and numbers.count(value)>1:
        #print("кол.во вхождений:",numbers.count(value))
        numbers_list += (value,)
        #indexes=[index for index,val in enumerate(numbers) if val==value]
        for index, val  in enumerate(numbers):
            if val==value:
                indexes += (index,)
        print(f"Индексы элемента {value}:",*indexes)
#print(numbers_list)

'''
print("\n<<<<< Task 2.2 Повторяющиеся элементы >>>>> ")
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
print("Данные:",numbers)
numbers_list=()
for value in numbers:
    indexes = ()
    if value not in numbers_list:
        numbers_list+=(value,)
        #for index,val in enumerate(numbers):
        #    if val==value:
        #        indexes+=(index,)
        indexes=[index for index,val in enumerate(numbers) if val==value]
        if len(indexes)>1:
            print(f"Индексы элемента {value}:", *indexes)







