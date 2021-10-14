class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} went on!')

    def stop(self):
        print(f'{self.name} stopped!')

    def turn_direction(self, direction):
        print(f'{self.name} changed direction: ', direction)

    def show_speed(self):
        print(f'Current speed of {self.name} is: ', self.speed)

    def show_attrs(self):
        print(f'About {self.name}:')
        print(f'Speed is: {self.speed} km/h')
        print('Color is:', self.color)
        print('Is it a police car? ', self.is_police)


class TownCar(Car):
    def show_speed(self):
        print(f'Current speed of {self.name} is: ', self.speed)
        if self.speed > 60:
            print('Attention! Your speed is higher than allowed (60 km/h)!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed of {self.name} is: ', self.speed)
        if self.speed > 40:
            print('Attention! Your speed is higher than allowed (40 km/h)!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car1 = WorkCar(43, 'blue', 'car1', False)
car1.show_attrs()
car1.go()
car1.show_speed()

print('********')

car2 = TownCar(0, 'green', 'car2', False)
car2.show_attrs()
car2.stop()
car2.show_speed()

print('********')

car3 = PoliceCar(80, 'black', 'car3', True)
car3.show_attrs()
car3.turn_direction('to the North')
car3.show_speed()

print('********')

car4 = SportCar(90, 'red', 'car1', False)
car4.show_attrs()
car4.turn_direction('to the East')
car4.show_speed()
