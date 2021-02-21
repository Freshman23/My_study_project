def cap_func(user_str):
    user_list = user_str.split(' ')
    cap_user_list = []
    for el in user_list:
        # С помощью встроенной функции capitalize():
        # cap_user_list.append(el.capitalize())
        #
        # Без помощи capitalize() и title(), работает только на латинице и кириллице:
        if (97 <= ord(el[0]) <= 122) or (1072 <= ord(el[0]) <= 1103):
            cap_el = chr(ord(el[0]) - 32) + el[1:]
        else:
            cap_el = el
        cap_user_list.append(cap_el)
    cap_user_str = ' '.join(cap_user_list)
    return cap_user_str


# С помощью встроенной функции title():
# print(input('Напишите слова с маленькой буквы через [пробел]:\n').title())
#
# Без помощи title():
print(cap_func(input('Напишите слова с маленькой буквы через [пробел]:\n')))
