number_month = int(input('Введите порядковый номер месяца в году: '))

# seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето',
#            'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
# print('Это', seasons[number_month - 1])

seasons = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for seas, months in seasons.items():
    if number_month in months:
        print('Это', seas)
        break
