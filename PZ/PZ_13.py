"""В матрице найти среднее арифметическое положительных элементов."""
def pos_element_mid(matrix):
    pos_elements = [element for row in matrix for element in row if element > 0]  # Поиск положительных элементов
    return sum(pos_elements) / len(pos_elements) if pos_elements else "В матрице нет положительных элементов"


matrix = [
    [1, 2, 3],
    [-4, -5, -6],
    [7, 8, 9]
]
number = pos_element_mid(matrix)
print("Среднее арифметическое положительных элементов = ", number)

