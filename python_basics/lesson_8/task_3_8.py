class NotANumberError(Exception):
    def __init__(self, txt='not a number has entered.'):
        self.txt = txt

    def __str__(self):
        return self.txt


def digitize(user_str):
    if user_str.isdigit():
        return int(user_str)
    else:
        try:
            return int(user_str)
        except ValueError:
            try:
                return float(user_str)
            except ValueError:
                return 'Not a number'


user_list = []
while True:
    user_input = input('Enter a number to add to user list or [quit] to finish the program: ')
    try:
        if digitize(user_input) != 'Not a number':
            user_list.append(digitize(user_input))
        elif user_input == 'quit':
            print('Program has finished. User list:', user_list)
            break
        else:
            raise NotANumberError
    except NotANumberError as err:
        print('Error:', err)
