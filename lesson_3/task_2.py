def data_collect(**kwargs):
    data_string = ', '.join(kwargs.values())
    return data_string

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')
print('Информация пользователя:', data_collect(name=name, surname=surname, birth=birth,
                                               town=town, email=email, phone=phone))
