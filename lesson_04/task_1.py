# в качестве основы я решил выбрать свое многострадальное четвертое задание из третьего урока. уж больно громоздкое
# получилось решение у меня - как раз хороший вариант для медленного и неэффективного кода
# с моего варианта решения и начнем
import random
import timeit
import cProfile


def my_array_max(min_value, max_value, size):
    array = [random.randint(min_value, max_value) for _ in range(size)]
    temp_array = []
    results_array = []
    for number in array:
        temp_dict = {'number': int, 'count': 0}
        for number_ in array:
            if number_ == number:
                temp_dict['number'] = number_
                temp_dict['count'] += 1
        temp_array.append(temp_dict)
    for element in temp_array:  # кстати, заодно избавился от среза всего массива вот тут...
        if element['count'] != 1:
            results_array.append(element)
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
print(timeit.timeit('my_array_max(0, 100, 20)', number=1000, globals=globals()))  # 0.07302596699992137
print(timeit.timeit('my_array_max(0, 100, 40)', number=1000, globals=globals()))  # 0.13341784099975484
print(timeit.timeit('my_array_max(0, 100, 80)', number=1000, globals=globals()))  # 0.2818127270002151
print(timeit.timeit('my_array_max(0, 100, 160)', number=1000, globals=globals()))  # 0.9640358310007286
print(timeit.timeit('my_array_max(0, 100, 320)', number=1000, globals=globals()))  # 3.4052604850003263
print(timeit.timeit('my_array_max(0, 100, 640)', number=1000, globals=globals()))  # 12.701947237999775
# тестируем с помощью сипрофайла с теми же условиями
cProfile.run('my_array_max(0, 100, 20)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        20    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:244(randint)
#        20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:9(my_array_max)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        21    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(0, 100, 40)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        40    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        40    0.000    0.000    0.000    0.000 random.py:244(randint)
#        40    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:9(my_array_max)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        52    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        40    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        52    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(0, 100, 80)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:9(my_array_max)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       124    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        80    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       100    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(0, 100, 160)')
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       160    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       160    0.000    0.000    0.000    0.000 random.py:244(randint)
#       160    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_1.py:10(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_1.py:9(my_array_max)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       283    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       160    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       201    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(0, 100, 320)')
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#       320    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       320    0.000    0.000    0.000    0.000 random.py:244(randint)
#       320    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_1.py:10(<listcomp>)
#         1    0.003    0.003    0.004    0.004 task_1.py:9(my_array_max)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#       626    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       320    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       408    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(0, 100, 640)')
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#       640    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       640    0.000    0.000    0.001    0.000 random.py:244(randint)
#       640    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.002    0.002 task_1.py:10(<listcomp>)
#         1    0.012    0.012    0.014    0.014 task_1.py:9(my_array_max)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#      1279    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       640    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       794    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

