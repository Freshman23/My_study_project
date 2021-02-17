from itertools import cycle

my_list = [2 ** x for x in range(5)]
cnt = 0
for num in cycle(my_list):
    print(num)
    cnt += 1
    if cnt >= 15:
        break
