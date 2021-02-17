init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_list = [num for num in init_list if init_list.count(num) == 1]
print(res_list)
