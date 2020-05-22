# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 15
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
BASE = 0
min_instance_counter = BASE
max_instance_counter = BASE
for idx, number_ in enumerate(array[:]):
    if number_ == min_value and min_instance_counter == 0:
        array[idx] = max_value
        min_instance_counter += 1
    if number_ == max_value and max_instance_counter == 0:
        array[idx] = min_value
        max_instance_counter += 1
print(*array)
