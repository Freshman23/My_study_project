def division():
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
    try:
        dividend/divider
    except ZeroDivisionError as err:
        print('Ошибка:', err)
        print('Говорят, что на ноль делить нельзя, НО при делителе -> 0 lim (делимое/делитель) =', chr(8734))
        return 'бесконечность'
    else:
        return dividend/divider


print('Частное от деления равно:', division())
