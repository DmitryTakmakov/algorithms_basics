# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Блок-схемы по ссылке: https://drive.google.com/file/d/1dfAzfS2SXg9Cn9Ox8RP-vJk_lCXgXHpr/view?usp=sharing

x = int(input('Введите трехзначное число: '))
x1 = x // 100
x2 = x % 100 // 10
x3 = x % 10
sum = x1 + x2 + x3
mult = x1 * x2 * x3
print(f'Сумма цифр вашего числа равна {sum}')
print(f'Произведение цифр вашего числа равна {mult}')

# это прям совсем на простых математических операторах решение, потому что я не уверен, допустимо ли по условиям урока
# сделать так: x1, x2, x3 = map(int, str(x))