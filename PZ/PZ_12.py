"""В последовательности из N чисел (N – чётное) во второй её половине найти сумму элементов больших 10."""
N = 8
numbers = [1, 34, 2, 3, 553, 10, 11, 12]
if N % 2 != 0 or len(numbers) % 2 != 0:  # Проверка условия на чётность длины последовательности
    print("Длина последовательности должна быть чётной")
else:
    second_half = sum(i for i in numbers[N // 2:] if i > 10)  # Генератор суммирующий элементы списка
    print(numbers)
    print("Сумма элементов больших 10 во второй половине последовательности: ", second_half)



































