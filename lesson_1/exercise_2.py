total_sec_amount = int(input('Введите количество секунд:'))
sec_amount = total_sec_amount % 60
total_min_amount = total_sec_amount // 60
min_amount = total_min_amount % 60
total_hour_amount = total_min_amount // 60
hour_amount = total_hour_amount % 24
day_amount = total_hour_amount // 24

print(f'{day_amount} дней\nВремя: {hour_amount:02d}:{min_amount:02d}:{sec_amount:02d}')
