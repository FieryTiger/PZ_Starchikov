"""Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
площади, длины окружности и диаметра.
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def lenght(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


radius = 20
print(f"Радиус круга: {radius}")
circle = Circle(radius)
area = circle.area()
print(f"Площадь круга: {area}")
lenght = circle.lenght()
print(f"Длина окружности: {lenght}")
diameter = circle.diameter()
print(f"Диаметр круга: {diameter}")