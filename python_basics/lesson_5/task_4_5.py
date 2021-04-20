numbers = ('Один', 'Два', 'Три', 'Четыре')
with open('task_4_5.txt', 'r') as file_read:
    with open('task_4_5_new.txt', 'a') as file_write:
        for line in file_read:
            num = int(line.split(" - ")[1])
            file_write.write(f'{numbers[num - 1]} - {num}\n')
