init_list = [123, 12, 34, 3, 4, 0, 1024, 512, 56, 1, 1, 5, 2, 4]
res_list = [el for ind, el in enumerate(init_list[1:]) if init_list[ind] < el]
print(res_list)
