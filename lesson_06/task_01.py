# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
Да, это более-менее ваше решение, но черт подери! я отталкивался от вашей функции, которую вы писали на уроке, и
попробовал сделать так, как вижу. ну, и потом одна сложность повлекла за собой другую, и в попытках это все решить, я и
пришел, по сути, к тому же самому! даже к фишке с основным кодом в приватном методе я в итоге пришел сам, потому что без
него код вылетал с RecursionError.
"""
import random
import sys


class MemoryChecker:

    def __init__(self):
        self._size = 0
        self._object_types = {}

    def check(self, *args):
        for item in args:
            self._memory_check(item)

    def _type_size(self, object):
        object_type = type(object)
        temp = sys.getsizeof(object)
        self._size += temp
        if object_type in self._object_types:
            self._object_types[object_type] += temp
        else:
            self._object_types[object_type] = temp

    def _memory_check(self, object):
        self._type_size(object)
        if hasattr(object, '__iter__'):
            if hasattr(object, 'items'):
                for key, value in object.items():
                    self._memory_check(key)
                    self._memory_check(value)
                    self._type_size(key)
                    self._type_size(value)
            elif not isinstance(object, str):
                for item in object:
                    self._memory_check(item)
                    self._type_size(item)

    def __str__(self):
        return f'Всего переменные заняли {self._size} байт.\n' + '\n'.join([f'Переменные {key} заняли {value} байт' for
                                                                            key, value in self._object_types.items()])


SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 200
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)

min_value = array[0]
max_value = array[0]
for number in array:
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number
print(f'Минимальный элемент в массиве - {min_value}, максимальный - {max_value}')
base = 0
min_instance_counter = base
max_instance_counter = base
for idx, number_ in enumerate(array[:]):
    if number_ == min_value and min_instance_counter == 0:
        array[idx] = max_value
        min_instance_counter += 1
    if number_ == max_value and max_instance_counter == 0:
        array[idx] = min_value
        max_instance_counter += 1
print(*array)

mem_check = MemoryChecker()
mem_check.check(array, min_value, max_value)
print(mem_check)
