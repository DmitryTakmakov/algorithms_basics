# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

FIRST_LETTER = 96
number = int(input('Введите порядковый номер буквы английского алфавита: '))
letter = chr(number + FIRST_LETTER)
print(f'Под номером {number} находится буква {letter}')
