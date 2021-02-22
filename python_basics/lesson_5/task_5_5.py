from random import randint
with open('task_5_5.txt', 'w+') as num_file:
    num_file.write(' '.join([str(randint(1, 9999)) for _ in range(20)]))
    num_file.seek(0)
    num_sum = 0
    for num in num_file.read().split(' '):
        num_sum = num_sum + int(num)
print(f'Sum of numbers from created file "{num_file.name}" is {num_sum}')
