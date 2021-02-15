user_list = (input('Введите строку с пробелами:\n')).split()

for index, word in enumerate(user_list):
    length = (10, len(word))[len(word) < 10]
    print(index + 1, word[:length])
