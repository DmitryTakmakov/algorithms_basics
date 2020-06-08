"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""


def hash_strings(string: str):
    hashes = {hash(string[0])}  # множество с хешем первого элемента строки. множество не примет повторяющиеся хеши
    for i in range(len(string)):
        substring = string[i:]  # отдельная подстрока-срез от i-того элемента для удобства дальнейшей работы
        j = len(substring)  # начальное значение второго итератора для цикла, идущего с конца среза, полученного во
        # внешнем цикле
        for _ in range(len(substring[:j])):
            if j < len(string) and len(substring[:j]) > 0:  # исключаем пустую подстроку и подстроку равную самой строке
                hashes.add(hash(substring[:j]))
            j -= 1
        i += 1
    return f'В строке {string} {len(hashes)} уникальных подстрок.'


a = 'papa'
print(hash_strings(a))
b = 'sova'
print(hash_strings(b))
c = 'abrakadabra'
print(hash_strings(c))
