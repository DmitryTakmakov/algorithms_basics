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


# функция готова, теперь пропускаем ее через таймит, увеличивая количество элементов массива в два раза в каждом тесте
print(timeit.timeit('my_array_max(0, 100, 20)', number=1000, globals=globals()))  # 0.0558772839995072
print(timeit.timeit('my_array_max(0, 100, 40)', number=1000, globals=globals()))  # 0.12037088500073878
print(timeit.timeit('my_array_max(0, 100, 80)', number=1000, globals=globals()))  # 0.3085587559999112
print(timeit.timeit('my_array_max(0, 100, 160)', number=1000, globals=globals()))  # 1.0253302529999928
print(timeit.timeit('my_array_max(0, 100, 320)', number=1000, globals=globals()))  # 3.4286873689998174
print(timeit.timeit('my_array_max(0, 100, 640)', number=1000, globals=globals()))  # 12.684498782000446
# тестируем с помощью сипрофайла с теми же условиями
cProfile.run('my_array_max(0, 100, 20)')
#        20    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:244(randint)
#        20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:9(my_array_max)
cProfile.run('my_array_max(0, 100, 40)')
#        40    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        40    0.000    0.000    0.000    0.000 random.py:244(randint)
#        40    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:9(my_array_max)
cProfile.run('my_array_max(0, 100, 80)')
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_1.py:9(my_array_max)
cProfile.run('my_array_max(0, 100, 160)')
#       160    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       160    0.000    0.000    0.000    0.000 random.py:244(randint)
#       160    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_1.py:10(<listcomp>)
#         1    0.002    0.002    0.002    0.002 task_1.py:9(my_array_max)
cProfile.run('my_array_max(0, 100, 320)')
#       320    0.000    0.000    0.001    0.000 random.py:200(randrange)
#       320    0.000    0.000    0.001    0.000 random.py:244(randint)
#       320    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_1.py:10(<listcomp>)
#         1    0.004    0.004    0.005    0.005 task_1.py:9(my_array_max)
cProfile.run('my_array_max(0, 100, 640)')
#       640    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       640    0.000    0.000    0.001    0.000 random.py:244(randint)
#       640    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.002    0.002 task_1.py:10(<listcomp>)
#         1    0.020    0.020    0.022    0.022 task_1.py:9(my_array_max)
