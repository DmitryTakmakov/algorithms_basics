# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
Да, это более-менее ваше решение, но черт подери!) я отталкивался от вашей функции, которую вы писали на уроке, и
попробовал сделать так, как вижу. ну, и потом одна сложность повлекла за собой другую, и в попытках это все решить, я и
пришел, по сути, к тому же самому! даже к фишке с основным кодом в приватном методе я в итоге пришел сам, потому что без
него код вылетал с RecursionError.
Из важного:
система Ubuntu 18.04, разрядность - 64 бита, версия интерпретатора - 3.8
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
            elif not isinstance(object, str):
                for item in object:
                    self._memory_check(item)

    def __str__(self):
        return f'Всего переменные заняли {self._size} байт.\n' + '\n'.join([f'Переменные {key} заняли {value} байт' for
                                                                            key, value in self._object_types.items()])


# вариант 1 - с урока
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

mem_check = MemoryChecker()
mem_check.check(array, min_value, max_value, min_instance_counter, max_instance_counter)
print(f'Первая реализация: \n{mem_check}')
print('*' * 100)
"""
Всего переменные заняли 37084 байт.
Переменные <class 'list'> заняли 9016 байт
Переменные <class 'int'> заняли 28068 байт
"""

# вариант 2, все то же самое, но со словарем (я уже говорил. что словари это по-пацански) и бонусным списком, потому что
# нигде не сказано, что варианты решений должны быть лучше имеющихся)
array_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array_2)

values = {min_value: array[0], max_value: array[0]}
for number in array:
    if number > values[max_value]:
        values[max_value] = number
    if number < values[min_value]:
        values[min_value] = number
print(f'Минимальный элемент в массиве - {values[min_value]}, максимальный - {values[max_value]}')
BASE = 0
min_instance_counter = BASE
max_instance_counter = BASE
a = array_2.copy()
for idx, number_ in enumerate(a):
    if number_ == values[min_value] and min_instance_counter == 0:
        a[idx] = values[max_value]
        min_instance_counter += 1
    if number_ == values[max_value] and max_instance_counter == 0:
        a[idx] = values[min_value]
        max_instance_counter += 1
print(*a)

mem_check = MemoryChecker()
mem_check.check(array_2, values, min_instance_counter, max_instance_counter, a)
print(f'Вторая реализация: \n{mem_check}')
print('*' * 100)
"""
Всего переменные заняли 73432 байт.
Переменные <class 'list'> заняли 17072 байт
Переменные <class 'int'> заняли 56128 байт
Переменные <class 'dict'> заняли 232 байт
"""

# а вместо третьего варианта той же задачки я использовал другую задачку! не казните, пожалуйста, просто хочу побыстрее
# с этим покончить и двинуться дальше. да и принципиально отличного с точки зрения переменных решения я так и не
# придумал. так что пусть будет многострадальная 4 задача из третьего урока.

array_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array_3)

results_array = []
temp_array = []
for number in array_3:
    temp_dict = {'number': int, 'count': 0}
    for number_ in array_3:
        if number_ == number:
            temp_dict['number'] = number_
            temp_dict['count'] += 1
    temp_array.append(temp_dict)
for element in temp_array:
    if element['count'] != 1:
        results_array.append(element)
max_count = 0
max_element = 0
for element_ in results_array:
    if element_['count'] > max_count:
        max_count = element_['count']
        max_element = element_['number']
if max_count != 0:
    print(f'В данном массиве число {max_element} встречается {max_count} раза.')
else:
    print('Все элементы данного массива встречаются только один раз.')

mem_check = MemoryChecker()
mem_check.check(array_3, results_array, temp_array, max_count, max_element)
print(f'Третья реализация, другая задача: \n{mem_check}')
"""
Всего переменные заняли 845868 байт.
Переменные <class 'list'> заняли 27048 байт
Переменные <class 'int'> заняли 139548 байт
Переменные <class 'dict'> заняли 462144 байт
Переменные <class 'str'> заняли 217128 байт
"""
