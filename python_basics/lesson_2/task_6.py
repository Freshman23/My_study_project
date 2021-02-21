num = 1
prod_specs = (input('Введите через [пробел] название, цену, количество и регистрационный номер'
                    'данного товара в наличии и нажмите [Enter]:\n')).split(' ')
prod_dict = dict(Name=prod_specs[0], Cost=prod_specs[1], Quantity=prod_specs[2], Reg_number=prod_specs[3])
# Создаем список кортежей с номером и словарем характеристик товара (по примеру №1):
prod_list = [(num, prod_dict)]
# Создаем словарь, где ключи - характеристики товара, значения - списки значений характеристик товара (по примеру №2):
total_prod_dict = dict(Name=[prod_specs[0]], Cost=[prod_specs[1]], Quantity=[prod_specs[2]], Reg_number=[prod_specs[3]])

while True:
    user_info = input(f'Аналогичным образом введите информацию по {num + 1}-му товару '
                      f'или наберите "continue" и нажмите [Enter] для формирования списка товаров:\n')
    if user_info == 'continue':
        break
    else:
        num += 1
        prod_specs = user_info.split(' ')
        prod_dict = dict(Name=prod_specs[0], Cost=prod_specs[1], Quantity=prod_specs[2], Reg_number=prod_specs[3])
        # Добавляем в список кортежи с информацией по дополнительным товарам:
        prod_list.append((num, prod_dict))
        # Дополняем значения словаря информацией по дополнителным товарам:
        total_prod_dict['Name'].append(prod_specs[0])
        total_prod_dict['Cost'].append(prod_specs[1])
        total_prod_dict['Quantity'].append(prod_specs[2])
        total_prod_dict['Reg_number'].append(prod_specs[3])

print(prod_list)
# Для наглядности списка лучше запустить этот цикл:
# print('[')
# for prod in prod_list:
#     print(prod)
# print(']')
print(total_prod_dict)
