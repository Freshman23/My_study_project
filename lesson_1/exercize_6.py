current_result = float(input('Каков текущий результат спортсмена в километрах? '))
goal = float(input('А какова его цель? '))
days = 1

while current_result < goal:
    current_result = 1.1 * current_result
    days = days + 1

print(f'Цель будет достигнута на {days}-й день')
