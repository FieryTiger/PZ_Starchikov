"""В матрице элементы первого столбца возвести в куб."""
def cube_element(matrix):
    return [[row[0] ** 3] + row[1:] for row in matrix if row]  # Возводит в куб первый элемент каждой строки


matrix = [
    [1, 2, 3],
    [-4, -5, -6],
    [7, 8, 9]
]
new_matrix = cube_element(matrix)
for row in new_matrix:
    print(row)
