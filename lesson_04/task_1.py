# в качестве основы я решил выбрать свое многострадальное четвертое задание из третьего урока. уж больно громоздкое
# получилось решение у меня - как раз хороший вариант для медленного и неэффективного кода

# с моего варианта решения и начнем
import random
import timeit
import cProfile


def my_array_max(size):
    array = [random.randint(0, 100) for _ in range(size)]
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
print(timeit.timeit('my_array_max(20)', number=10000, globals=globals()))  # 0.421552256000723
print(timeit.timeit('my_array_max(40)', number=10000, globals=globals()))  # 0.9387782869998773
print(timeit.timeit('my_array_max(80)', number=10000, globals=globals()))  # 2.753190261999407
print(timeit.timeit('my_array_max(160)', number=10000, globals=globals()))  # 9.154586634000225
print(timeit.timeit('my_array_max(320)', number=10000, globals=globals()))  # 33.02670952299923
print(timeit.timeit('my_array_max(640)', number=10000, globals=globals()))  # 124.65933747099916
# тестируем с помощью сипрофайла с теми же условиями
cProfile.run('my_array_max(20)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        20    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:244(randint)
#        20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_01.py:9(my_array_max)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        21    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(40)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        40    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        40    0.000    0.000    0.000    0.000 random.py:244(randint)
#        40    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_01.py:9(my_array_max)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        52    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        40    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        52    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(80)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_01.py:9(my_array_max)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       124    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        80    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       100    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(160)')
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       160    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       160    0.000    0.000    0.000    0.000 random.py:244(randint)
#       160    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_01.py:10(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_01.py:9(my_array_max)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       283    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       160    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       201    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(320)')
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#       320    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       320    0.000    0.000    0.000    0.000 random.py:244(randint)
#       320    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_01.py:10(<listcomp>)
#         1    0.003    0.003    0.004    0.004 task_01.py:9(my_array_max)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#       626    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       320    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       408    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('my_array_max(640)')
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#       640    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       640    0.000    0.000    0.001    0.000 random.py:244(randint)
#       640    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.002    0.002 task_01.py:10(<listcomp>)
#         1    0.012    0.012    0.014    0.014 task_01.py:9(my_array_max)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#      1279    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       640    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       794    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# второй вариант - немного схитрим и используем второй вариант решения преподавателя с урока, со словарем. потому что
# словарь - это по-пацански :)


def teacher_array_max(size):
    array = [random.randint(0, 100) for _ in range(size)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    if num is not None:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'


# тестируем эту функцию с теми же условиями - увеличивая количество элементов в два раза с каждым тестом
print(timeit.timeit('teacher_array_max(20)', number=10000, globals=globals()))  # 0.23247075200015388
print(timeit.timeit('teacher_array_max(40)', number=10000, globals=globals()))  # 0.3897852869995404
print(timeit.timeit('teacher_array_max(80)', number=10000, globals=globals()))  # 0.7419532499989145
print(timeit.timeit('teacher_array_max(160)', number=10000, globals=globals()))  # 1.4201540630001546
print(timeit.timeit('teacher_array_max(320)', number=10000, globals=globals()))  # 2.835826996999458
print(timeit.timeit('teacher_array_max(640)', number=10000, globals=globals()))  # 5.672430847000214
# шик, теперь - сипрофайл
cProfile.run('teacher_array_max(20)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        20    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:244(randint)
#        20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:120(teacher_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:121(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        22    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('teacher_array_max(40)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        40    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        40    0.000    0.000    0.000    0.000 random.py:244(randint)
#        40    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:120(teacher_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:121(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        40    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        49    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('teacher_array_max(80)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:120(teacher_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:121(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        80    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       103    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('teacher_array_max(160)')
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       160    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       160    0.000    0.000    0.000    0.000 random.py:244(randint)
#       160    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_01.py:120(teacher_array_max)
#         1    0.000    0.000    0.001    0.001 task_01.py:121(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       160    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       221    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('teacher_array_max(320)')
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       320    0.000    0.000    0.001    0.000 random.py:200(randrange)
#       320    0.000    0.000    0.001    0.000 random.py:244(randint)
#       320    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_01.py:120(teacher_array_max)
#         1    0.000    0.000    0.001    0.001 task_01.py:121(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       320    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       393    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('teacher_array_max(640)')
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#       640    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       640    0.000    0.000    0.002    0.000 random.py:244(randint)
#       640    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.002    0.002 task_01.py:120(teacher_array_max)
#         1    0.000    0.000    0.002    0.002 task_01.py:121(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       640    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       805    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# третий вариант. ох, как же хотелось здесь использовать какой-нибудь Counter)) ну, пусть будет метод count - он
# хотя бы созвучен, да и какого-то прям радикально другого решения для этой задачи я так и не придумал, увы :'(


def stupid_array_max(size):
    array = [random.randint(0, 100) for _ in range(size)]
    max_number = array[0]
    max_ = 0
    for number in array:
        temp_c = array.count(number)
        if temp_c > 1:
            if temp_c > max_:
                max_ = temp_c
                max_number = number
    if max_ != 0:
        return f'Число {max_number} встречается в массиве {max_} раз(а).'
    else:
        return f'Все числа в массиве встречаются по одному разу.'


# я прекрасно отдаю себе отчет, что это, по сути, ваше решение, переписанное с методом count, но если я буду и дальше
# биться головой в эту задачу, то я рискую не доделать это задание и к следующему дедлайну. наверное, я просто тупой.

print(timeit.timeit('stupid_array_max(20)', number=10000, globals=globals()))  # 0.25043038799776696
print(timeit.timeit('stupid_array_max(40)', number=10000, globals=globals()))  # 0.5532171669983654
print(timeit.timeit('stupid_array_max(80)', number=10000, globals=globals()))  # 1.45620129800227
print(timeit.timeit('stupid_array_max(160)', number=10000, globals=globals()))  # 4.517073426002753
print(timeit.timeit('stupid_array_max(320)', number=10000, globals=globals()))  # 15.735445995000191
print(timeit.timeit('stupid_array_max(640)', number=10000, globals=globals()))  # 59.754649876995245

cProfile.run('stupid_array_max(20)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        20    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:244(randint)
#        20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:218(stupid_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:219(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        20    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        24    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('stupid_array_max(40)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        40    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        40    0.000    0.000    0.000    0.000 random.py:244(randint)
#        40    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:218(stupid_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:219(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        40    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        40    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        48    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('stupid_array_max(80)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 task_01.py:218(stupid_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:219(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        80    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        80    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       104    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('stupid_array_max(160)')
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       160    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       160    0.000    0.000    0.000    0.000 random.py:244(randint)
#       160    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 task_01.py:218(stupid_array_max)
#         1    0.000    0.000    0.000    0.000 task_01.py:219(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       160    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       160    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       194    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('stupid_array_max(320)')
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#       320    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       320    0.000    0.000    0.001    0.000 random.py:244(randint)
#       320    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.002    0.002 task_01.py:218(stupid_array_max)
#         1    0.000    0.000    0.001    0.001 task_01.py:219(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       320    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       320    0.002    0.000    0.002    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       409    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('stupid_array_max(640)')
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#       640    0.001    0.000    0.001    0.000 random.py:200(randrange)
#       640    0.000    0.000    0.001    0.000 random.py:244(randint)
#       640    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.009    0.009 task_01.py:218(stupid_array_max)
#         1    0.000    0.000    0.002    0.002 task_01.py:219(<listcomp>)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#       640    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       640    0.007    0.000    0.007    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       822    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""
Вывод:
В принципе, во всех вариантах функции наблюдается линейный рост - при увеличении N в два раза времени на выполнение
затрачивается в 3 раза больше, кроме второго варианта - там прямая не столь резко взлетает вверх.
Что и делает второй вариант самой лучшей реализацией из представленных, что, впрочем, и не удивительно.
"""
