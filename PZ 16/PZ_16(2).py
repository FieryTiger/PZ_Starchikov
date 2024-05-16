"""Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления площади, длины окружности и диаметра
(с использованием pickle и функций)."""
import math
import pickle


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def length(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


method = [Circle.area, Circle.length, Circle.diameter]


def save_def(method, filename):
    with open(filename, 'wb') as f:
        pickle.dump(method, f)


def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


radius = 10
circle = Circle(radius)
area = circle.area()
length = circle.length()
diameter = circle.diameter()

save_def(Circle.area, 'area.bin')
save_def(Circle.length, 'length.bin')
save_def(Circle.diameter, 'diameter.bin')

loaded_area = load_def('area.bin')
loaded_length = load_def('length.bin')
loaded_diameter = load_def('diameter.bin')

print(f"Радиус круга: {radius}, Площадь: {loaded_area(circle)}, Длина окружности: {loaded_length(circle)}, Диаметр круга: {loaded_diameter(circle)}")