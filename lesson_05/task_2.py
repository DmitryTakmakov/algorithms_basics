"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

HEXADECIMAL = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def my_hex_in(string):
    for key, value in HEXADECIMAL.items():
        if string == key:
            return value


def my_hex_out(integer):
    for key, value in HEXADECIMAL.items():
        if integer == value:
            return key


def hex_sum(a: deque, b: deque):
    a = a.copy()
    b = b.copy()
    if len(a) > len(b):
        while len(b) < len(a):
            b.appendleft('0')
    else:
        while len(a) < len(b):
            a.appendleft('0')

    a = deque(reversed(a))
    b = deque(reversed(b))
    result = deque()
    for idx, element in enumerate(b):
        if len(result) > 0 and result[0] == 1:
            temp = my_hex_in(element) + my_hex_in(a[idx]) + result.popleft()
            if temp == 16:
                result.append('1')
            elif temp > 16:
                result.appendleft(my_hex_out(temp % 16))
                result.appendleft(1)
            else:
                result.appendleft(my_hex_out(temp))
        else:
            temp = my_hex_in(element) + my_hex_in(a[idx])
            if temp == 16:
                result.append('1')
            elif temp > 16:
                result.appendleft(my_hex_out(temp % 16))
                result.appendleft(1)
            else:
                result.appendleft(my_hex_out(temp))
    return result


number_1 = deque(input('Введите шестнадцатеричное число: '))
number_2 = deque(input('Введите еще одно шестнадцатеричное число: '))
sum_ = hex_sum(number_1, number_2)

print(f'Результат сложения чисел: {list(sum_)}')
