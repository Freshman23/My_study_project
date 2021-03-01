class Clothes:
    def __init__(self, name):
        self.name = name
        self.clothes = []

    def add_coat(self, name, height, amount=1):
        for _ in range(amount):
            self.clothes.append(Coat(name, height))

    def add_suit(self, name, size, amount=1):
        for _ in range(amount):
            self.clothes.append(Suit(name, size))

    @property
    def get_clothes(self):
        return [(item.name, item.mat_amount) for item in self.clothes]

    @property
    def total_mat_amount(self):
        return sum([item.mat_amount for item in self.clothes])


class Coat:
    def __init__(self, name, height):
        self.name = name
        self.mat_amount = 2 * height + 0.3


class Suit:
    def __init__(self, name, size):
        self.name = name
        self.mat_amount = round(size / 12.5 + 0.5, 2)


g = Clothes('Wardrobe')
g.add_coat('Ted Baker', 1.9)
g.add_suit('Hugo Boss', 50, 3)
print(f'Clothes list in {g.name}: {g.get_clothes}')
print(f'Total amount of material used to make clothes to {g.name}: {g.total_mat_amount} sq.m.')
