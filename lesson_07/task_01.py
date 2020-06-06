"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
"""
import random


def reverse_bubble_sort(array: list):
    array = array.copy()
    n = 1
    is_sorted = False
    """
    это счетчик на случай, если массив был уже отсортирован, чтобы не гонять алгоритм почем зря.
    вот такую простенькую рекомендацию по улучшению сортировки пузырьком я нашел в интернете :)
    но алгоритм действительно умнее себя ведет - всего лишь 1 проход цикла, если загонять туда уже заранее 
    отсортированный массив.
    """
    while n < len(array):
        if not is_sorted:
            is_sorted = True
            for i in range(len(array) - 1):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    is_sorted = False
            n += 1
        else:
            break

    return array


SIZE = 10
arr = [random.randint(-100, 99) for i in range(SIZE)]
print(f'Массив до сортировки: {arr}')
a = reverse_bubble_sort(arr)
print(f'Отсортированный по убыванию массив: {a}')
