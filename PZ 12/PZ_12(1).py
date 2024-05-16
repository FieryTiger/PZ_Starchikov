"""Составить генератор (yield), который выводит из строки только буквы."""


def generator(input_str):  # Функция генератор, проверяющая строку на наличие букв
    for i in input_str:
        if i.isalpha():
            yield i


input_str = "serdftvgbh 12345 @#$%^&RWFD@23"
letters = ', '.join(generator(input_str))  # Вызов функции с объединением букв в строку
print("Изначальная строка: ", input_str)
print("Буквы со строки: ", letters)
