'''Task 1. Электронное письмо
Реализуйте класс Email, который представляет электронное письмо.
Каждое письмо должно содержать:
   + sender — адрес отправителя
   + recipient — адрес получателя
   + subject — тема письма
   + body — текст письма
   + date — дата отправки

Класс должен поддерживать:
Сравнение писем по дате
Преобразование письма в строку
Получение длины текста письма
Проверку на наличие текста в письме или
не состоит ли текст только из пробелов

Пример использования:
e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

Пример вывода:
From: alice@example.com
To: bob@example.com
Subject: Meeting
- Let's meet at 10am -
From: bob@example.com
To: alice@example.com
Subject: Report
-  -
Length: 18
Has text: True
Is newer: True
'''
print("Task 1. Электронное письмо")
from functools import total_ordering
from datetime import datetime

@total_ordering
class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date  # import from datetime

    # Сравнение писем по дате
    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    # Преобразование письма в строку
    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n- {self.body} -\n"

    # Получение длины текста письма
    def __len__(self):
        return len(self.body)

    # Проверку на наличие текста в письме или
    # не состоит ли текст только из пробелов
    def __bool__(self):
        return bool(self.body.strip())  # löschen leertasten

# main code
e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)

print("Length:", len(e1))
print("Has text:", bool(e1))    # Has text: True
print("Has text:", bool(e2))    # Has text: False

print("Is newer:", e2 > e1)     # Is newer: True (e2:(2024, 6, 11), e1:(2024, 6, 10))



########################################################################
'''Task 2. Класс для работы с деньгами
Создайте класс Money, в котором можно:
   + складывать и вычитать объекты через операторы + и -
   + выводить объект как строку в виде "$<amount>"
   + при сложении и вычитании возвращается новый объект
   + если вычитание приводит к отрицательному значению — вернуть 0

Пример использования: 
money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

Пример вывода: 
$150
$50
$0
'''
print()
print("*"*40)
print("Task 2. Класс для работы с деньгами")

class Money:
    def __init__(self, amount):
        self.amount = amount

    # складывать и вычитать объекты через операторы + и -
    # при сложении и вычитании возвращается новый объект
    def __add__(self, other):
        return Money(self.amount + other.amount)

    # если вычитание приводит к отрицательному значению — вернуть 0
    def __sub__(self, other):
        result = self.amount - other.amount
        return Money(max(result, 0))    # 0 > -1

    #  выводить объект как строку в виде "$<amount>"
    def __str__(self):
        return f"${self.amount}"

# main code
money1 = Money(100)
#print(money1)
money2 = Money(50)

print(money1 + money2)  # $150
print(money1 - money2)  # $50
print(money2 - money1)  # $0

