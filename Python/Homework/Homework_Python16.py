'''Task 1. Оценки текстом
Напишите программу, которая преобразует список оценок по системе от 1 до 5
в текстовое представление. Нужно сохранить в списках числовой результат и
текстовое представление.
Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно".
Данные:
grades = [5, 3, 4, 2, 1, 5, 3]
Пример вывода:
[[5, 'отлично'], [3, 'хорошо'], [4, 'хорошо'], [2, 'неудовлетворительно'],
[1, 'неудовлетворительно'], [5, 'отлично'], [3, 'хорошо']]
'''
print("\n<<<<< Task 1.1 Оценки текстом >>>>>")
grades = [5, 3, 4, 2, 1, 5, 3]
grades_new=[]
for item in grades:
    match item:
        case 5:
            grades_new.append([5,'отлично'])
        case 4 | 3:
            grades_new.append([item,'хорошо'])
        case _:
            grades_new.append([item, 'неудовлетворительно'])
print(grades_new)

print("\n<<<<< Task 1.2 Оценки текстом >>>>>")
grades = [5, 3, 4, 2, 1, 5, 3]
grades_new=[[item,'отлично'] if item == 5
            else ([item,'хорошо'] if item == 3 | 4
                  else [item, 'неудовлетворительно']) for item in grades]
print(grades_new)


print("\n<<<<< Task 1.4 Оценки текстом >>>>>")
grades = [5, 3, 4, 2, 1, 5, 3]
for i in range(len(grades) - 1, -1, -1):  # идём от конца к началу
    grade = grades[i]
    if grade == 5:
        grades[i] = [grade, 'отлично']
    elif grade in (3, 4):
        grades[i] = [grade, 'хорошо']
    else:
        grades[i] = [grade, 'неудовлетворительно']

print(grades)




'''Task 2. Правильные скобки
Напишите программу, которая принимает строку, содержащую любые виды скобок — круглые (), 
квадратные [] и фигурные {}.
Необходимо проверить, правильно ли они расставлены. 
Скобки считаются правильно расставленными, если:
Каждая открывающая скобка имеет соответствующую закрывающую.
Скобки закрываются в правильном порядке.
Пример данных:
string = "({[}])"

Пример вывода:
Скобки: ({[}])
Валидны: False

Скобки: ([({}()){}])
Валидны: True
'''

print("\n<<<<< Task 2.1 Правильные скобки >>>>>")
string = "([({}()){}])"
output_string=string
l=len(string)
if l%2 !=0:
    print(f"Скобки:{string}\nВалидны: False (нечетное число скобок)")
else:
    test=''
    while test != string:
        test=string
        #print(test)
        string = string.replace("()","")
        string = string.replace("{}", "")
        string = string.replace("[]", "")
# Если строка стала пустой, значит всё было корректно
    is_valid = (string == "")
    print(f"Скобки: {output_string}\nВалидны: {is_valid}")

print("\n<<<<< Task 2.2 Правильные скобки >>>>>")
string = "([({}()){}])"
#string = "[}{]"
stack = []
if len(string) % 2 != 0:
    print(f"Скобки: {string}\nВалидны: False (нечётное число скобок)")
else:
    valid = True            # Считаем, что скобки валидные
    for char in string:
        if char in '([{':
            stack.append(char)

        # Для каждой закрывающей скобки задаём, какая должна быть открывающая
        elif char in ')]}':
            if char == ')':
                expected = '('
            elif char == ']':
                expected = '['
            elif char == '}':
                expected = '{'

            # Если стек !!пустой!! ИЛИ скобка !!НЕ!! соответствует ожидаемой
            if not stack or stack[-1] != expected:
                valid = False
                break

            # Скобки совпали — удаляем верхнюю из стека (удаляем правый(последний) элемент из стека)
            stack.pop()

    # После обработки всех скобок (скобки верные И стэк пустой):
    if valid and not stack:
        print(f"Скобки: {string}\nВалидны: True")
    else:
        print(f"Скобки: {string}\nВалидны: False")

