with open('task_1_5.txt', 'a') as f_wr:
    while True:
        user_in = input('Введите строку и нажмите [Enter] для записи в файл'
                        ' или оставьте строку пустой и нажмите [Enter] для завершения работы:\n')
        if user_in != '':
            f_wr.write(user_in + '\n')
        else:
            break
print(f'Работа программы завершена. Вся информация сохранена в файл: {f_wr.name}')
