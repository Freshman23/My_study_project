total_sum = 0
quit_mark = False


def number_sum_func(number_str):
    str_list = number_str.split(' ')
    number_list = []
    global total_sum, quit_mark
    for num in str_list:
        if num.isdigit():
            number_list.append(int(num))
        elif num == 'quit':
            quit_mark = True
            break
    total_sum = total_sum + sum(number_list)


number_sum_func(input('Введите числа для суммирования через [пробел]:\n'))
print('Общая сумма:', total_sum)
while True:
    number_sum_func(input('Продолжите ввод чисел через [пробел] для суммирования '
                    'или введите "quit" для завершения программы:\n'))
    if quit_mark:
        print('Общая сумма:', total_sum)
        print('Программа завершена.')
        break
    else:
        print('Общая сумма:', total_sum)
