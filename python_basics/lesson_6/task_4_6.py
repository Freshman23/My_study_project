class Car:
    _speed_limits = {'work': 40, 'in_town': 60, 'speedway': 90}

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} goes at a speed of {speed} km/h.')

    def stop(self):
        self.speed = 0
        print(f'{self.name} stopped.')

    def turn(self, direct):
        if self.speed != 0:
            print(f'{self.name} turned {direct} and continues going at a speed of {self.speed} km/h.')
        else:
            print(f'{self.name} has to go to turn somewhere.')

    def show_speed(self):
        print(f'The current speed of {self.name} is {self.speed} km/h.')


class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


class TownCar(Car):

    def show_speed(self):
        if self.speed > super()._speed_limits['in_town']:
            print(f'Warning! The allowed limit of {super()._speed_limits["in_town"]} km/h exceeded.', end=' ')
        super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        if self.speed > super()._speed_limits['work']:
            print(f'Warning! The allowed limit of {super()._speed_limits["work"]} km/h exceeded.', end=' ')
        super().show_speed()


class SportCar(Car):

    def show_speed(self):
        if self.speed < super()._speed_limits['speedway']:
            print('Put the pedal to the metal, dude! This car can do better;)', end=' ')
        super().show_speed()


t = TownCar('Renault Logan', 'pink')
w = WorkCar('Caterpillar', 'orange')
s = SportCar('BMW i8', 'grey-blue')
p = PoliceCar('Chevrolet Camaro', 'aqua')

t.go(60)
t.turn('left')
w.go(60)
w.show_speed()
w.stop()
s.go(60)
s.show_speed()
s.go(120)
p.turn('back')
p.go(120)
p.turn('back')
print('')
print(t.__dict__)
print(w.__dict__)
print(s.__dict__)
print(p.__dict__)
