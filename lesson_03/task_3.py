# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)

min_value = MAX_ITEM  # если здесь также оставить 0, то там всегда 0 и будет
max_value = MIN_ITEM
for number in array:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number
print(f'Минимальный элемент в массиве - {min_value}, максимальный - {max_value}')
for idx, number_ in enumerate(array[:]):
    if number_ == min_value:
        array[idx] = max_value
    if number_ == max_value:
        array[idx] = min_value
print(*array)
