''' 1. Таблица умножения
Напишите программу, которая выводит таблицу умножения для чисел от 1 до n.
 Где n это число, которое введет пользователь.
 Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)
Пример вывода:
Введите число: 5
print("\n<<<<<   Task 1.1 Таблица умножения   >>>>>")
n=int(input("Введите число: "))
for y in range(1,n+1):
    for x in range(1, n + 1):
        i=y*x
        if x < n and i<10:
            print(i,end="    ")
        elif x < n and i>=10:
            print(i,end="   ")
        else:
            print(i)
'''
print("\n<<<<<   Task 1.2 Таблица умножения   >>>>>")
n = int(input("Введите число: "))
for y in range(1, n + 1):
    for x in range(1, n + 1):
        print(y * x, end="\t")  # Используем табуляцию для выравнивания
    print()  # Переход на новую строку после каждой строки таблицы


'''2. Лестница чисел
Напишите программу, которая принимает число n и выводит "лестницу" из чисел. 
Каждая строка лестницы содержит числа от 1 до номера строки.
Пример вывода:
Введите число: 5  
print("\n<<<<<   Task 2.1 Лестница чисел   >>>>>")
n=int(input("Введите число: "))
for num_str in range(1,n+1):
    for x in range(1, num_str + 1):
        if x < (num_str + 1):
            print(x,end=" ")
        elif x<(num_str+1) and x>=10:
            print(x,end="")
        else:
            print(x)
    print() #переход на новую строку
'''
print("\n<<<<<   Task 2.2 Лестница чисел   >>>>>")
n = int(input("Введите число: "))
for num_str in range(1, n + 1):
    for x in range(1, num_str + 1):
        print(x, end=" ")  # Выводим числа в строке
    print()    #переход на новую строку


''' 3. Удаление всех повторяющихся символов
Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы, 
сохраняя только первые их вхождения.
Пример вывода:
Введите строку: Python programming  
Результат: Python prgami
'''
print("\n<<<<<   Task 3.1 Удаление всех повторяющихся символов   >>>>>")
user_input = input("Введите строку: ")
lenth=len(user_input)
text_rezult=""
for char in user_input:
    if char in text_rezult:
        continue
    else:
        text_rezult+=char
        #print(text_rezult)
print("Результат:",text_rezult)