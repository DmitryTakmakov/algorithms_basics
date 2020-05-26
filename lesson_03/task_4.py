# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)

'''
я не удивлюсь, если нормальное решение этой задачи записывается типа в 5-10 строчек кода. но я так долго думал именно
над подобным решением, что в итоге попал в ловушку "туннельного зрения" - я просто не вижу другого, без всех этих
циклов в циклах, за которыми идут еще циклы и ветвления. ну, что ж, ради этого мы тут и собрались - чтобы учиться!
'''
results_array = []  # готовим массив для ответов
for number in array:
    temp_dict = {'number': int, 'count': 0}
    for number_ in array:  # перебираем все числа в массиве
        if number_ == number:
            temp_dict['number'] = number_
            temp_dict['count'] += 1
    results_array.append(temp_dict)
for element in results_array[:]:  # удаляем те, что встречаются только один раз
    if element['count'] == 1:
        results_array.remove(element)
max_count = 0
max_element = 0
for element_ in results_array:  # будем считать, что при условии, когда несколько чисел встречаются одинаковое
    # количество раз, я выбрал отобразить только одно из них
    if element_['count'] > max_count:
        max_count = element_['count']
        max_element = element_['number']
if max_count != 0:
    print(f'В данном массиве число {max_element} встречается {max_count} раза.')
else:  # это на случай, если нет элементов, встречающихся чаще 1 раза
    print('Все элементы данного массива встречаются только один раз.')
