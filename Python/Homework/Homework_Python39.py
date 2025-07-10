'''Task 1. Фигуры и площади
Создайте абстрактный класс Shape.
В классе должен быть метод area(), который возвращает площадь фигуры.
Реализуйте два класса:
Circle, который принимает радиус.
Rectangle, который принимает ширину и высоту.

Task 2. Проверка размеров фигур
Доработайте фигуры:
Добавьте проверку в конструкторы Circle и Rectangle,
чтобы значения были положительными.
Если передано отрицательное или нулевое значение,
выбрасывайте пользовательское исключение InvalidSizeError.
'''
from abc import ABC, abstractmethod
import math

class InvalidSizeError(ValueError):
    """ Raised when shape dimensions are invalid"""
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return "shape (abstract)"

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("radius must be > 0")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle, radius = {self.radius}"

class Rechtangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("width and height must be > 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rechtangle, width:height = {self.width}:{self.height}"

# main code
#shapes = [Circle(3), Rechtangle(4,5)]

shapes = []
try:
    shapes.append(Circle(-3))
except InvalidSizeError as e:
    print("Error: creating shape -", e)     # Error: creating shape - radius must be > 0

try:
    shapes.append(Circle(3))
except InvalidSizeError as e:
    print("Error: creating shape -", e)

try:
    shapes.append(Rechtangle(4,0))
except InvalidSizeError as e:
    print("Error: creating shape -", e)     #Error: creating shape - width and height must be > 0

try:
    shapes.append(Rechtangle(4,5))
except InvalidSizeError as e:
    print("Error: creating shape -", e)

for shape in shapes:
    print(f"Area ({shape.__str__()}): {shape.area():.2f}")
