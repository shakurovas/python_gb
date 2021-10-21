class OfficeEquipmentWarehouse:
    pass


class OfficeEquipment:
    def __init__(self, name, quantity, cost, format):
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.format = format


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, cost, format, is_color, printing_technology, cartridge_number):
        super().__init__(name, quantity, cost, format)
        self.printing_technology = printing_technology
        self.is_color = is_color
        self.cartridge_number = cartridge_number


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, cost, format, scan_speed, sensor_type):
        super().__init__(name, quantity, cost, format)
        self.scan_speed = scan_speed
        self.sensor_type = sensor_type


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, cost, format, is_color, screen_resolution):
        super().__init__(name, quantity, cost, format)
        self.is_color = is_color
        self.screen_resolution = screen_resolution
