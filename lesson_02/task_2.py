# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

users_number = input('Введите любое натуральное число: ')
even_counter = 0
uneven_counter = 0
for digit in users_number:
    if int(digit) % 2 == 0:
        even_counter += 1
    else:
        uneven_counter += 1
print(f'В данном числе {even_counter} четных цифры и {uneven_counter} нечетных цифры.')
