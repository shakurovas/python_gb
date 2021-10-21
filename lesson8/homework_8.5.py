class OfficeEquipmentWarehouse:

    warehouse_status = {'Scanner': 0, 'Xerox': 0, 'Printer': 0}
    it_dep_status = {'Xerox': 0, 'Scanner': 0, 'Printer': 0}
    learning_centre_dep_status = {'Xerox': 0, 'Scanner': 0, 'Printer': 0}
    hr_dep_status = {'Xerox': 0, 'Scanner': 0, 'Printer': 0}
    deps_status = {'it_dep': it_dep_status, 'learning_centre_dep': learning_centre_dep_status, 'hr_dep': hr_dep_status}

    def acceptance_to_warehouse(self, what_to_accept):
        for key, value in what_to_accept.items():
            if key in self.warehouse_status.keys():  # if such item is already in warehouse
                self.warehouse_status.update({key: value+self.warehouse_status[key]})
            else:  # if such item is not yet in warehouse
                self.warehouse_status.update({key: value})

        print(what_to_accept, ' was accepted to warehouse')
        print('Now in warehouse: ', self.warehouse_status)

    def sending_to(self, what_to_send, where_to):
        if where_to in self.deps_status.keys():  # if the name of department is in our dict of deps
            for key, value in what_to_send.items():
                if key in self.warehouse_status.keys() and value <= self.warehouse_status[key]:
                    if key in self.deps_status[where_to].keys():  # if such item is already in warehouse of this dep
                        self.deps_status[where_to].update({key: value + self.deps_status[where_to][key]})
                    else:  # if such item is not yet in warehouse of this dep
                        self.deps_status[where_to].update({key: value})
                    print(what_to_send[key], 'items of', key, f'was/were sent to {where_to}')
                    self.warehouse_status[key] -= value
                else:
                    print('Can not send number of items less than there is now in the common warehouse!')
        else:
            print('There is no such dep in our Office!')
        print(f'Now in {where_to}: ', self.deps_status[where_to])
        print('Now in warehouse: ', self.warehouse_status)


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


wh1 = OfficeEquipmentWarehouse()
wh1.acceptance_to_warehouse({'Scanner': 6, 'Xerox': 2, 'Printer': 4})
print('******')
wh1.acceptance_to_warehouse({'Xerox': 5})
print('******')
wh1.sending_to({'Xerox': 3}, 'learning_centre_dep')
print('******')
wh1.sending_to({'Xerox': 4, 'Scanner': 1}, 'hr_dep')
print('******')
wh1.sending_to({'Xerox': 18, 'Scanner': 18, 'Printer': 1}, 'it_dep')
