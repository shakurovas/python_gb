class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass_for_meter, thickness):
        print('Asphalt mass needed: ', (self._length * self._width * mass_for_meter * thickness) / 1000, 'ton')


my_road1 = Road(20, 5000).asphalt_mass(25, 5)
