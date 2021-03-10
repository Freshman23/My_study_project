from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    _warranty_term: int
    _specifications: dict

    def __init__(self, name, model, vendor_code):
        self.name = name
        self.model = model
        self.vendor_code = vendor_code

    def __str__(self):
        return f'{self.__class__.__name__.lower()} {self.name} {self.model}'

    @abstractmethod
    def get_specifications(self):
        return f'Specifications of {self.__class__.__name__.lower()} {self.name} {self.model}: ' \
               f'vendor code - {self.vendor_code}'

    @abstractmethod
    def get_warranty_info(self):
        pass


class Printer(OfficeEquipment):
    _warranty_term = 18
    _specifications = {'HP GP-230': 'type - ink-jet, print speed - 20 sh/min, dimensions - 40cm*30cm*20cm'}

    @property
    def get_specifications(self):
        return f'{super().get_specifications()}, ' \
               f'{Printer._specifications.get(f"{self.name} {self.model}")}.'

    @classmethod
    def get_warranty_info(cls):
        return f'Warranty terms for printers: {cls._warranty_term} month.'


class Scanner(OfficeEquipment):
    _warranty_term = 12
    _specifications = {'Canon Scan_LiDE_400': 'type - flatbed, scan speed - 10 sh/s, dimensions - 40cm*30cm*5cm'}

    @property
    def get_specifications(self):
        return f'{super().get_specifications()}, ' \
               f'{Scanner._specifications.get(f"{self.name} {self.model}")}.'

    @classmethod
    def get_warranty_info(cls):
        return f'Warranty conditions and terms for scanners: {cls._warranty_term} month.'


class CopyMachine(OfficeEquipment):
    _warranty_term = 24
    _specifications = {'Xerox ABC-1000': 'type - digit, print speed - 50sh/s, '
                                         'scan speed - 30 sh/s, dimensions - 60cm*60cm*90cm'}

    @property
    def get_specifications(self):
        return f'{super().get_specifications()}, ' \
               f'{CopyMachine._specifications.get(f"{self.name} {self.model}")}.'

    @classmethod
    def get_warranty_info(cls):
        return f'Warranty conditions and terms for copy machines: {cls._warranty_term} month.'


class Warehouse:
    _goods = []
    _notation_list = []
    _goods_map = {'printer': Printer, 'scanner': Scanner, 'copymachine': CopyMachine}

    @classmethod
    def get_goods(cls, number=0):
        if number == 0:
            return [el[0] for el in cls._goods]
        else:
            return cls._goods[number - 1][0]

    @classmethod
    def form_not_list(cls):
        cls._notation_list = [(obj[0].__class__.__name__.lower(), obj[0].name, obj[0].model) for obj in cls._goods]

    @classmethod
    def full_goods_info(cls):
        goods_str = f'{30 * "*"}\nCurrent information about goods in the warehouse:\n'
        if not cls._goods:
            goods_str += 'There are not goods at the warehouse yet.\n'
        else:
            for ind, obj in enumerate(cls._goods):
                goods_str += f'{ind + 1}. {obj[0]}, amount: {obj[1]}\n'
        print(goods_str[:-1])

    @classmethod
    def accept_good(cls, good, name, model, amount, vendor_code):
        if (cls._goods == []) or not ((good, name, model) in cls._notation_list):
            cls._goods.append([Warehouse._goods_map[good](name, model, vendor_code), amount])
        else:
            ind = cls._notation_list.index((good, name, model))
            cls._goods[ind][1] += amount
        cls.form_not_list()
        print(f'{amount} {good}/s {name} {model} has/have been accepted at the warehouse.')

    @classmethod
    def issue_good(cls, good, name, model, amount, department):
        if (good, name, model) in cls._notation_list:
            ind = cls._notation_list.index((good, name, model))
            if amount < cls._goods[ind][1]:
                cls._goods[ind][1] -= amount
                print(f'{amount} {good}/s {name} {model} has/have been issued to {department}.')
            else:
                print(f'The last {cls._goods[ind][1]} {good}/s {name} {model} has/have been issued to {department}.')
                del cls._goods[ind]
            cls.form_not_list()
        else:
            print(f'There is not {good} {name} {model} at the warehouse to issue to {department}.')


Warehouse.accept_good('printer', 'HP', 'GP-230', 6, 'OEp0001')
Warehouse.accept_good('scanner', 'Canon', 'Scan_LiDE_400', 6, 'OEs0001')
Warehouse.accept_good('copymachine', 'Xerox', 'ABC-1000', 3, 'OEcm0001')
# Warehouse.accept_good('printer', 'HP', 'GP-230', 2, 'OEp0001')
# Warehouse.accept_good('copymachine', 'Xerox', 'ABC-1000', 2, 'OEcm0001')
# print()
# print(Warehouse.full_goods_info())
# print()
# Warehouse.issue_good('printer', 'HP', 'GP-230', 4, 'Headquarters')
# Warehouse.issue_good('scanner', 'Canon', 'Scan_LiDE_400', 3, 'Headquarters')
# Warehouse.issue_good('copymachine', 'Xerox', 'ABC-1000', 3, 'Headquarters')
# print()
# print(Warehouse.full_goods_info())
# print()
# Warehouse.issue_good('printer', 'HP', 'GP-230', 3, 'HR')
# Warehouse.issue_good('scanner', 'Canon', 'Scan_LiDE_400', 3, 'HR')
# Warehouse.issue_good('copymachine', 'Xerox', 'ABC-1000', 3, 'HR')
# Warehouse.issue_good('copymachine', 'Xerox', 'ABC-1000', 1, 'Archive')
# Warehouse.accept_good('scanner', 'Canon', 'Scan_LiDE_400', 1, 'OEs0001')
# Warehouse.accept_good('copymachine', 'Xerox', 'ABC-1000', 1, 'OEcm0001')
# print()
# print(Warehouse.full_goods_info())
# print()
# printer = Warehouse.get_goods()[0][0]
# print(printer.get_specifications)
# print(printer.get_warranty_info())
# scanner = Warehouse.get_goods()[1][0]
# print(scanner.get_specifications)
# print(scanner.get_warranty_info())
# copymachine = Warehouse.get_goods()[2][0]
# print(copymachine.get_specifications)
# print(copymachine.get_warranty_info())

navigation = {'accept': Warehouse.accept_good,
              'issue': Warehouse.issue_good,
              'info': Warehouse.full_goods_info,
              'spec': Warehouse.get_goods}

print(30 * '*' + '\nWelcome to The Warehouse!\n'
      'Enter command "accept" to accept some good at the warehouse.\n'
      'Enter "printer", "scanner" or "copymachine" after command to specify a type of good.\n'
      'Then enter "name", "model", "amount" and "vendor code" of good.\n'
      'All words should be entered through a space. E.g.[accept printer HP GP-230 3 #eo0001]\n'
      'Enter command "issue" to issue good to somewhere. E.g. [issue printer HP GP-230 3 Headquarters]\n'
      'Enter command "info" to display info of goods at the warehouse. E.g. [info]\n'
      'Enter command "spec" and "number" to display specifications of good from info list. E.g. [spec 2]')
while True:
    user_request = input(30 * '*' + '\nEnter the command: ')
    if user_request == 'quit':
        print('The program has ended.')
        break
    else:
        try:
            user_request_list = user_request.split(' ')
            if len(user_request_list) >= 5 and user_request_list[4].isdigit():
                user_request_list[4] = int(user_request_list[4])
                navigation.get(user_request_list[0])(*user_request_list[1:])
            if len(user_request_list) == 1:
                navigation.get(user_request_list[0])()
            if len(user_request_list) == 2:
                num = int(user_request_list[1])
                print(navigation.get(user_request_list[0])()[num - 1].get_specifications)
        except Exception as err:
            print('Error:', err, '\nThe command has been entered incorrectly. Try again.')
