rat_list = [7, 5, 3, 3, 2]
print('Структура рейтингов:', rat_list)

while len(rat_list) < 15:  # ввод до 15 значений
    user_num = int(input('Введите число, чтобы добавить его в структуру: '))
    if user_num in rat_list:
        position = len(rat_list) - rat_list[::-1].index(user_num)
        rat_list.insert(position, user_num)
    elif user_num < rat_list[len(rat_list) - 1]:
        rat_list.append(user_num)
    else:
        for position, num in enumerate(rat_list):
            if user_num > num:
                rat_list.insert(position, user_num)
                break
    print('Обновленная структура рейтингов:', rat_list)
