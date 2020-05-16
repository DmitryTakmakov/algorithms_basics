# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randrange, uniform

print("Задайте границы. Введите либо два целых числа, либо два вещественных числа, либо два символа."
      "Главное, чтобы нижняя и верхняя границы совпадали")
a = input("Введите нижнюю границу: ")
b = input("Введите верхнюю границу: ")
if a.isdigit() and b.isdigit():
    print(randrange(int(a), int(b) + 1))
elif a.isalpha() and b.isalpha():
    print(chr(randrange(ord(a), ord(b) + 1)))
else:
    print(uniform(float(a), float(b)))
