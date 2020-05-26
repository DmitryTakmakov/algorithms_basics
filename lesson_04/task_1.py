# в качестве основы я решил выбрать свое многострадальное четвертое задание из третьего урока. уж больно громоздкое
# получилось решение у меня - как раз хороший вариант для медленного и неэффективного кода
# с моего варианта решения и начнем
import random
import timeit
import cProfile


def my_array_max(min_value, max_value, size):
    array = [random.randint(min_value, max_value) for _ in range(size)]
    results_array = []
    for number in array:
        temp_dict = {'number': int, 'count': 0}
        for number_ in array:
            if number_ == number:
                temp_dict['number'] = number_
                temp_dict['count'] += 1
        results_array.append(temp_dict)
    for element in results_array[:]:
        if element['count'] == 1:
            results_array.remove(element)
    max_count = 0
    max_element = 0
    for element_ in results_array:
        if element_['count'] > max_count:
            max_count = element_['count']
            max_element = element_['number']
    if max_count != 0:
        return f'В данном массиве число {max_element} встречается {max_count} раза.'
    else:
        return 'Все элементы данного массива встречаются только один раз.'


# функция готова, теперь пропускаем ее через таймит
print(timeit.timeit('my_array_max(0, 100, 20)', globals=globals()))
