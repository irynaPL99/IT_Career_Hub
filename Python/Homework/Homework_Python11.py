''' Task 1. Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-*** '''

print(("\n<<<<< Task 1.1 Звёздочки вместо чисел >>>>>"))
text = "My number is 123-456-789"
new_text=""
print("Строка:", text)
for char in text:
    if char.isdigit():
        char="*"
    new_text+=char
print("Результат:", new_text)

'''
print(("\n<<<<< Task 1.2 Звёздочки вместо чисел >>>>>"))
text = "My number is 123-456-789"
new_text=""
print("Строка:", text)
new_text="".join("*" if char.isdigit() else char for char in text)
print("Результат:", new_text)
'''

''' Task 2. Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке. 
Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только один раз.
text = "Programming in python"
Пример вывода:
Строка: Programming in python
Символ 'p' встречается 2 раз(а)
Символ 'r' встречается 2 раз(а)
Символ 'o' встречается 2 раз(а)
Символ 'g' встречается 2 раз(а)
Символ 'm' встречается 2 раз(а)
Символ 'i' встречается 2 раз(а)
Символ 'n' встречается 3 раз(а)
Символ ' ' встречается 2 раз(а) '''

print(("\n<<<<< Task 2. Количество символов >>>>>"))
text = "Programming in python"
print("Строка:",text)
text=text.lower()
char_list=[]
for char in text:
    if char in char_list:
        continue
    if text.count(char) !=0 and text.count(char)>1:
        print("Символ",char,"встречается",text.count(char),"раз(а)")
        char_list+=char

'''Task 3. Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
'''
print(("\n<<<<< Task 3. Увеличение чисел >>>>>"))
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
list=text.split()
#print(len(list),list)
for i in range(0,len(list)-1):
    #print(type(list[i]))
    if (list[i].isnumeric() or                                      # если это число без точки
            list[i].count(".")==1 and list[i].replace('.', '').isdigit()) : # если это число с точкой
        #list[i]= float(list[i])*10
        list[i]=str(float(list[i])*10)
        #print(list[i])
#new_text=' '.join(list)
#print(new_text)
print(' '.join(list))



