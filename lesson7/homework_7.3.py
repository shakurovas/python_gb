from math import ceil


class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    def __add__(self, other):
        return self.num_of_cells + other.num_of_cells

    def __sub__(self, other):
        if self.num_of_cells - other.num_of_cells > 0:
            return self.num_of_cells - other.num_of_cells
        else:
            print('Can not subtract num of second cell from the first given one. Try to change their places. Or maybe they are equal')

    def __mul__(self, other):
        return self.num_of_cells * other.num_of_cells

    def __truediv__(self, other):
        if self.num_of_cells >= other.num_of_cells:
            return self.num_of_cells // other.num_of_cells
        else:
            print('Please, change the places of given cells and try again')

    def make_order(self, cell_num_in_row):
        counter = 0
        for i in range(ceil(self.num_of_cells / cell_num_in_row)):
            if self.num_of_cells - counter * cell_num_in_row >= cell_num_in_row:
                for j in range(cell_num_in_row):
                    print('*', end='')
                print()
                counter += 1
            else:
                for j in range(self.num_of_cells - counter * cell_num_in_row):
                    print('*', end='')
                print()


cell1 = Cell(4)
cell2 = Cell(13)
print(cell2 * cell1)
print(cell2 / cell1)
print(cell2 + cell1)
print(cell2 - cell1)
cell2.make_order(5)
