class Matrix:
    new_list = []

    def __init__(self, list_of_lines):
        self.list_of_lines = list_of_lines

    def __str__(self):
        for row in self.list_of_lines:  # перебираем строки матрицы
            for elem in row:  # перебираем элементы в строке матрицы
                print(elem, end=' ')
            print()
        return str()

    def __add__(self, other):
        if not self.list_of_lines:
            return 'The second matrix is not given'
        elif not other.list_of_lines:
            return 'The first matrix is not given'
        elif len(self.list_of_lines) != len(other.list_of_lines) or len(self.list_of_lines[0]) != len(other.list_of_lines[0]):
            return 'Can not sum 2 matrix of different size'
        else:
            for k in range(len(self.list_of_lines)):
                self.new_list.append([])
            for i in range(len(self.list_of_lines)):  # перебираем строки матрицы
                for j in range(len(self.list_of_lines[i])):  # перебираем элементы строки матрицы
                    self.new_list[i].append(self.list_of_lines[i][j] + other.list_of_lines[i][j])
            return self.new_list


matrix1 = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
matrix2 = Matrix([[-1, -1, -2], [-3, -4, -5], [-6, -7, -8]])
matrix3 = Matrix([[-1, -1], [-3, -4], [-6, -7]])
matrix4 = Matrix([[-1, -1, -2], [-3, -4, -5]])
matrix5 = Matrix([[-1, -1], [-3, -4]])
matrix6 = Matrix([])

print(matrix1 + matrix2)
print(matrix1 + matrix3)
print(matrix1 + matrix4)
print(matrix1 + matrix5)
print(matrix1 + matrix6)
