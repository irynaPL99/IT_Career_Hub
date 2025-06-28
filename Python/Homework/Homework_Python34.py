'''Task 1. Класс Rectangle
Создайте класс Rectangle, который описывает прямоугольник.
У каждого объекта должны быть два поля: width и height.
Добавьте метод get_area(), который возвращает площадь прямоугольника.
Создайте объект прямоугольника с произвольными значениями.
Выведите его площадь.
Измените ширину и высоту.
Выведите новую площадь.
'''
print("\nTask 1. Класс Rectangle")
class Rectangle:
# constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

# metod
    def get_area(self):
        return self.width * self.height

# create object
rect = Rectangle(3, 4)     # width, height
print("Площадь:", rect.get_area())

# update width, height
rect.width = 5
rect.height = 6

print("Новая площадь:", rect.get_area())


'''Task 2. Класс Counter
Реализуйте класс Counter, который представляет собой 
простой счётчик.
Счётчик должен начинаться с нуля.
Предусмотрите методы для увеличения и уменьшения значения 
на единицу, при этом при каждой операции должно 
отображаться новое значение счётчика.
Добавьте метод, возвращающий текущий результат.
Проверьте работу счётчика, выполнив несколько операций.
'''
print("\nTask 2. Класс Counter")
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value +=1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrement(self):
        self.value -=1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get_value(self):
        return self.value

# create object
counter = Counter()

# example using:
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
print("Текущее значение:", counter.get_value())




