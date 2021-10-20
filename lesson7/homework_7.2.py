from abc import ABC, abstractmethod


class Clothes(ABC):  # main class
    def __init__(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):  # child class 1
    def __init__(self, v):
        super().__init__()
        self.v = v

    def fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):  # child class 2
    def __init__(self, h):
        super().__init__()
        self.h = h

    def fabric_consumption(self):
        return 2 * self.h + 0.3


class CommonFabricConsumption:  # composition class, which counts total fabric consumption
    def __init__(self, list_obj):
        self.list_obj = list_obj

    @property
    def total_fabric_consumption(self):
        summation = 0
        for obj in self.list_obj:
            summation += obj.fabric_consumption()
        return summation


costume1 = Costume(1.63)
print(costume1.fabric_consumption())

coat1 = Coat(44)
print(coat1.fabric_consumption())

list_obj1 = [costume1, coat1]
total = CommonFabricConsumption(list_obj1)
print(total.total_fabric_consumption)
