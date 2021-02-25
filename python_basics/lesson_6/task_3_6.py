class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Engineer(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


a = Engineer('Jack', 'Peterson', 'engineer', 3000, 1000)
print('Worker full name is', a.get_full_name())
print('Worker income is', a.get_total_income())
