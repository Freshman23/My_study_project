class Road:

    def __init__(self, length, width):
        """length, width - длина и ширина дорожного полотна в метрах."""
        self._length = length
        self._width = width

    def total_mass_calc(self, spec_mass, thick_road):
        """spec_mass - масса в кг одного квадратного метра полотна толщиной в один сантиметр;
           thick_road - толщина дорожного полотна в см."""
        self.spec_mass = spec_mass
        self.thick_road = thick_road
        return self._length * self._width * self.spec_mass * thick_road


road = Road(2000, 10)
tot_mass = road.total_mass_calc(20, 10)
print(road.__dict__)
print(f'Общая масса дорожного полотна с указанными параметрами: {round(tot_mass / 1000)} т')
