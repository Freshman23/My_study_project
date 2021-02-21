def fact(num):
    prod = 1
    for el in range(num + 1):
        prod = (1, prod * el)[el > 0]
        yield prod


for ind, val in enumerate(fact(10)):
    print(f'{ind:3}! = {val}')
