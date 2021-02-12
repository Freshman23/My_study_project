def power_func(number, degree):
    ''' Первый способ:
        elevate = number ** degree

        Второй способ:'''
    elevate = 1
    for cur_degree in range(1, abs(degree) + 1):
        if degree >= 0:
            elevate = elevate * number
        else:
            elevate = elevate / number
    return elevate

number = float(input('Введите вещественное число: '))
degree = int(input('Введите отрицательное целое число в качестве степени: '))
print(power_func(number, degree))
