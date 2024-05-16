"""
Дано множество A из N точек (N > 2, точки заданы своими координатами x, у).
Найти такую точку из данного множества, сумма расстояний от которой до остальных его точек минимальна, и саму эту сумму.
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2 .
Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс, второй — для хранения ординат.
"""
import math

x_cords = [5, 8, 16]
y_cords = [3, 4, -9]
distance_sum = []
if len(x_cords) > 2 and len(y_cords) > 2:  # Проверка, что есть минимум 3 точки
    for x, y in zip(x_cords, y_cords):
        distances = []  # Cписок для хранения расстояний от текущей точки до всех остальных
        c_point = (x, y)
        for x1, y1 in zip(x_cords, y_cords):
            point = (x1, y1)
            if point != c_point: # Проверка, что это не текущая точка
                distance = math.sqrt((x1-x)**2+(y1-y)**2)
                distances.append(distance)
        distances_sum = sum(distances)
        distance_sum.append(distances_sum)
    min_sum = min(distance_sum)
    min_sum_point_index = distance_sum.index(min_sum)  # Индекс точки с минимальной суммой расстояний
    min_sum_point = (x_cords[min_sum_point_index], y_cords[min_sum_point_index])
    print("Точка минимальной суммы расстояний:", min_sum_point)
    print("Минимальная сумма расстояний:", min_sum)
else:
    print("Вы ввели меньше трёх точек")
