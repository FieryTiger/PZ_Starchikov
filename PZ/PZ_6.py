"""Дан список ненулевых целых чисел размера N.
Проверить, чередуются ли в нем положительные и отрицательные числа.
Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента, нарушающего закономерность."""

def check(lst):
    for i in range(len(lst) - 1):
        if lst[i] * lst[i + 1] > 0:  # проверяем, одного ли знака соседние числа
            return i + 1  # возвращаем порядковый номер(индекс)
    return 0  # числа чередуются


A = [1, -2, 3, 4, 5, -6]
print("Список A:", A)
print(check(A))
