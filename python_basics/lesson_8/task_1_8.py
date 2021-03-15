class Date:
    def __init__(self, date_str):
        self.date_list = Date.transform_date(date_str)

    @classmethod
    def transform_date(cls, date_str):
        try:
            date_list = [int(el) for el in date_str.split('-')]
        except ValueError as err:
            print('Error:', err)
            print('The entered date has an incorrect format.')
        else:
            return date_list

    @staticmethod
    def valid_date(date_list):
        try:
            if 1 <= date_list[0] <= 31 and 1 <= date_list[1] <= 12 and 1900 <= date_list[2] <= 2021:
                print('The entered date is valid.')
            else:
                print('The entered date has an invalid day, month and/or year.')
        except TypeError as err:
            print('This method is not possible.')


date = Date(input('Input date of format [dd-mm-yyyy]: '))
print(date.date_list)
Date.valid_date(date.date_list)
