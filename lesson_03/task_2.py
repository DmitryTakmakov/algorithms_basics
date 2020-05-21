# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array_1)
array_2 = []
for idx, number in enumerate(array_1):
    if number % 2 == 0:
        array_2.append(idx)
print(*array_2)
