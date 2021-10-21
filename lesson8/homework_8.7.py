class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    @staticmethod
    def are_valid(num_1, num_2):
        if type(num_1) == int and type(num_2) == int:
            return True
        else:
            print('Can not count such numbers!')
            exit(-1)

    def __add__(self, other):
        if self.are_valid(self.re, self.im) and self.are_valid(other.re, other.im):
            sum_re = self.re + other.re
            sum_im = self.im + other.im
            if '-' in str(sum_im):
                add_result = str(sum_re) + str(sum_im) + 'i'
            else:
                add_result = str(sum_re) + '+' + str(sum_im) + 'i'
            return add_result

    def __mul__(self, other):
        if self.are_valid(self.re, self.im) and self.are_valid(other.re, other.im):
            sum = self.re * other.im + self.im * other.re
            diff = self.re * other.re - self.im * other.im
            if '-' in str(sum):
                mul_result = str(diff) + str(sum) + 'i'
            else:
                mul_result = str(diff) + '+' + str(sum) + 'i'
            return mul_result


num1 = ComplexNum(-4, -5)
num2 = ComplexNum(8, -32)
print(num1 + num2)
print(num1 * num2)
