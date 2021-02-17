from functools import reduce


def prod_num(num_1, num_2):
    return num_1 * num_2


form_list = [num for num in range(100, 1001) if num % 2 == 0]
print('Количество цифр в произведении чисел списка:', len(str(reduce(prod_num, form_list))))

# Можно и взглянуть на него:
# print(reduce(prod_num, form_list))
