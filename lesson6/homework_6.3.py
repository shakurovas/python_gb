class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_income_dict(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print('Total income:', self.get_income_dict()['wage'] + self.get_income_dict()['bonus'])


new_worker1 = Position('Svetlana', 'Shakurova', 'team-lead', {'wage': 550000, 'bonus': 50000})
new_worker1.get_full_name()
new_worker1.get_total_income()
