# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def summator(number):
    if number % 10 == number:
        return number
    else:
        return number % 10 + summator(number // 10)


max_sum = 0
max_number = 0
user_number = 1
while user_number != 0:
    user_number = int(input('Введите любое натуральное число, если вы хотите закончить, введите 0: '))
    temp_sum = summator(user_number)
    if temp_sum > max_sum:
        max_sum = temp_sum
        max_number = user_number
print(f'Из всех введеных чисел наибольшим по сумме цифр было {max_number}, сумма его чисел равна {max_sum}')
