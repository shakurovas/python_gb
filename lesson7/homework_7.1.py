def max_lines(matrix_1, matrix_2):
    if len(matrix_1) >= len(matrix_2):
        return len(matrix_1)
    else:
        return len(matrix_2)


def max_elems(matrix_1, matrix_2):
    if len(matrix_1[0]) >= len(matrix_2[0]):
        return len(matrix_1[0])
    else:
        return len(matrix_2[0])


def min_lines(matrix_1, matrix_2):
    if len(matrix_1) <= len(matrix_2):
        return len(matrix_1)
    else:
        return len(matrix_2)


def min_elems(matrix_1, matrix_2):
    if len(matrix_1[0]) <= len(matrix_2[0]):
        return len(matrix_1[0])
    else:
        return len(matrix_2[0])


def equal_all(list1, list2, new_list=[]):
    for k in range(len(list1)):
        new_list.append([])
    for i in range(max_lines(list1, list2)):  # перебираем строки матрицы вплоть до количества строк матрицы с самых их большим количеством
        for j in range(max_elems(list1, list2)):
            new_list[i].append(list1[i][j] + list2[i][j])
    return new_list


def equal_only_rows(list1, list2, new_list=[]):  # если количество строк в матрицах одинаковое, а количество элементов в строке разное
    for k in range(len(list1)):
        new_list.append([])
    if len(list1[0]) > len(list2[0]):  # если элементов в строке больше в первой матрице
        for i in range(len(list1)):
            for j in range(len(list2[0])):
                new_list[i].append(list1[i][j] + list2[i][j])
            for j in range(len(list2[0]), len(list1[0])):
                new_list[i].append(list1[i][j])
    else:  # если элементов в строке больше во второй матрице
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                new_list[i].append(list1[i][j] + list2[i][j])
            for j in range(len(list1[0]), len(list2[0])):
                new_list[i].append(list2[i][j])
    return new_list


def equal_only_elems(list1, list2, new_list=[]): # если количество элементов в строках матриц одинаковое, но разное количество рядов
    for k in range(max_lines(list1, list2)):
        new_list.append([])
    if len(list1) > len(list2):  # если строк больше в первой матрице
        for i in range(len(list2)):
            for j in range(len(list1[0])):
                new_list[i].append(list1[i][j] + list2[i][j])
        for i in range(len(list2), len(list1)):
            for j in range(len(list1[0])):
                new_list[i].append(list1[i][j])
    else:  # если строк больше во второй матрице
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                new_list[i].append(list1[i][j] + list2[i][j])
        for i in range(len(list1), len(list2)):
            for j in range(len(list2[0])):
                new_list[i].append(list2[i][j])
    return new_list


def nothing_is_equal(list1, list2, new_list=[]):
    for k in range(max_lines(list1, list2)):
        new_list.append([])
    for i in range(min_lines(list1, list2)):
        for j in range(min_elems(list1, list2)):
            new_list[i].append(list1[i][j] + list2[i][j])
        for j in range(min_elems(list1, list2), max_elems(list1, list2)):
            if max_elems(list1, list2) == len(list1[0]):
                new_list[i].append(list1[i][j])
            else:
                new_list[i].append(list2[i][j])
    for i in range(min_lines(list1, list2), max_lines(list1, list2)):
        if max_lines(list1, list2) == len(list1):
            for j in range(len(list1[0])):
                new_list[i].append(list1[i][j])
        else:
            for j in range(len(list2[0])):
                new_list[i].append(list2[i][j])
    return new_list


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
            return Matrix(other.list_of_lines)
        elif not other.list_of_lines:
            return Matrix(self.list_of_lines)
        elif len(self.list_of_lines) == len(other.list_of_lines) and len(self.list_of_lines[0]) == len(other.list_of_lines[0]):
            self.new_list = equal_all(self.list_of_lines, other.list_of_lines)
            return Matrix(self.new_list)
        elif len(self.list_of_lines) == len(other.list_of_lines) and len(self.list_of_lines[0]) != len(other.list_of_lines[0]):
            self.new_list = equal_only_rows(self.list_of_lines, other.list_of_lines)
            return Matrix(self.new_list)
        elif len(self.list_of_lines) != len(other.list_of_lines) and len(self.list_of_lines[0]) == len(other.list_of_lines[0]):
            self.new_list = equal_only_elems(self.list_of_lines, other.list_of_lines)
            return Matrix(self.new_list)
        else:
            self.new_list = nothing_is_equal(self.list_of_lines, other.list_of_lines)
            return Matrix(self.new_list)


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
