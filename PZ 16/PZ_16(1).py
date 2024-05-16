""" Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
"Человек". Каждый класс должен иметь метод, который выводит информацию о
поле объекта.
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "мужской")

    def sex_1(self):
        return f'{self.name}, {self.age} - мужчина'

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'женский')

    def sex_2(self):
        return f'{self.name}, {self.age} - женщина'


man = Man('Олег', 12)
woman = Woman('Оля', 15)
print(man.sex_1())
print(woman.sex_2())