# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)

min_value = array[0]
min_index = 0
max_value = array[0]
max_index = 0
for idx, number in enumerate(array):
    if number > max_value:
        max_value = number
        max_index = idx
    if number < min_value:
        min_value = number
        min_index = idx
print(f'Минимальный элемент в массиве - {min_value}, его индекс - {min_index}, максимальный - {max_value}, его индекс'
      f' - {max_index}.')
sum_ = 0
if min_index < max_index:
    for number_ in array[min_index + 1: max_index]:
        sum_ += number_
else:
    for number__ in array[max_index + 1: min_index]:
        sum_ += number__
print(f'Сумма чисел между минимальным и максимальным элементами массива равна {sum_}.')
