my_list = (input('Введите через запятую элементы списка:\n')).split(',')
end = (len(my_list) - 2, len(my_list) - 1)[len(my_list) % 2 == 0]

for ind, el in enumerate(my_list[:end:2]):
    my_list[2*ind], my_list[2*ind+1] = my_list[2*ind+1], my_list[2*ind]
print(my_list)
