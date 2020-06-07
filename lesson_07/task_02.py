"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def sorter(left_array: list, right_array: list):
    sorted_list = []
    i = 0
    j = 0
    for _ in range(len(left_array) + len(right_array)):
        if i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                sorted_list.append(left_array[i])
                i += 1
            else:
                sorted_list.append(right_array[j])
                j += 1
        elif i == len(left_array):
            sorted_list.append(right_array[j])
            j += 1
        elif j == len(right_array):
            sorted_list.append(left_array[i])
            i += 1
    return sorted_list


def merger_sorter(array: list):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merger_sorter(array[:mid])
    right_array = merger_sorter(array[mid:])

    return sorter(left_array, right_array)


SIZE = 10
arr = [random.uniform(0, 49) for _ in range(SIZE)]
print('Исходный массив вещественных чисел:')
print(*arr, sep='\n')
print('*' * 50)
a = merger_sorter(arr)
print('Отсортированный массив вещественных чисел:')
print(*a, sep='\n')
