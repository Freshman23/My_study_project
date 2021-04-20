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


worker = Engineer('Jack', 'Peterson', 'engineer', 3000, 1000)
print(worker.__dict__)
print('Worker full name is', worker.get_full_name())
print('Worker income is', worker.get_total_income())
