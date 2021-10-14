class Stationery:
    title = 'stationery'

    def draw(self):
        print('Drawing begins...')


class Pen(Stationery):
    title = 'pen'

    def draw(self):
        print(f'Drawing by {self.title} begins...')


class Pencil(Stationery):
    title = 'pencil'

    def draw(self):
        print(f'Drawing by {self.title} begins...')


class Handle(Stationery):
    title = 'handle'

    def draw(self):
        print(f'Drawing by {self.title} begins...')


my_stationery1 = Pen()
my_stationery1.draw()

my_stationery2 = Pencil()
my_stationery2.draw()

my_stationery3 = Handle()
my_stationery3.draw()
