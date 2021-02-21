from itertools import count

for num in count(3):
    if num > 10:
        break
    print(num)
