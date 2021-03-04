class SelfZeroDivisionError(Exception):
    def __init__(self, txt='trying division by zero has performed.'):
        self.txt = txt

    def __str__(self):
        return self.txt


a = int(input('Enter divide: '))
b = int(input('Enter divider: '))
try:
    if b == 0:
        raise SelfZeroDivisionError
except SelfZeroDivisionError as err:
    print('Error:', err)
else:
    print('Division result is', a / b)
