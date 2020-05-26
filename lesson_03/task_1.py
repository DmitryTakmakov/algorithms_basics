# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

range_ = [2, 3, 4, 5, 6, 7, 8, 9]
for digit in range_:
    division_counter = 0
    for number in range(2, 100):
        if number % digit == 0:
            division_counter += 1
    print(f'Цифра: {digit}, количество кратных ей чисел: {division_counter}')
