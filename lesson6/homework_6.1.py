import time


class TrafficLight:
    __color = 'red'

    def running(self):
        if self.__color == 'red':
            print(self.__color)
            time.sleep(7)
            self.__color = 'yellow'

        if self.__color == 'yellow':
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'

        if self.__color == 'green':
            print(self.__color)
            time.sleep(5)
            self.__color = 'red'


my_traffic_light = TrafficLight()
my_traffic_light.running()
