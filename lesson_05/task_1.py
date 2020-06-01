"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple('Company', ['company_name', 'q1', 'q2', 'q3', 'q4'])
instances = int(input('Укажите количество компаний: '))
i = 0
companies = []
global_income = 0
while i in range(instances):
    company = Company(
        input('Введите имя компании: '),  # я вот сначала сделал, а потом подумал - вероятно не стоит присваивать
        # значения таким образом, да?
        float(input('Введите прибыль за первый квартал: ')),
        float(input('Введите прибыль за второй квартал: ')),
        float(input('Введите прибыль за третий квартал: ')),
        float(input('Введите прибыль за четвертый квартал: ')))
    companies.append(company)
    global_income += company.q1 + company.q2 + company.q3 + company.q4
    i += 1

median_income = global_income / len(companies)
print(f'Средняя прибыль: {median_income}')

for company_ in companies:
    name, q1, q2, q3, q4 = company_
    profit = q1 + q2 + q3 + q4
    if profit < median_income:
        print(f'Компания {name} заработала меньше среднего.')
    if profit > median_income:
        print(f'Компания {name} заработала больше среднего.')
