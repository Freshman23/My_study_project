class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing.')


class Pen(Stationery):

    def draw(self):
        print(f'This pen "{self.title}" draws smooth and unobtrusive lines. Magnificent!')


class Pencil(Stationery):

    def draw(self):
        print(f'This pencil "{self.title}" draws thick and clear lines. Excellent!')


class Handle(Stationery):

    def draw(self):
        print(f'Damn! "{self.title}" dried up. There is no trust in these handles=(')


pen = Pen('Parker')
pencil = Pencil('Koh-I-Noor')
handle = Handle('Copic')
pen.draw()
pencil.draw()
handle.draw()
