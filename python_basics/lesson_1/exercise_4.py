positive_integer = int(input('Введите целое полодительное число: '))
current_integer = positive_integer
max_numeral = 0

while current_integer > 0:
    current_numeral = current_integer % 10
    if current_numeral > max_numeral:
        max_numeral = current_numeral
    current_integer = current_integer // 10

print(f'Максимальная цифра из числа: {positive_integer} - "{max_numeral}"')
