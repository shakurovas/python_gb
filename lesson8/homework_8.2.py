class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


divisible = float(input('Give a number-divisible here: '))
divider = float(input('Give a number-divider here (it should be not 0): '))
try:
    if divider == 0:
        raise ZeroException('Divider should not be zero!!!')
except ZeroException as err:
    print(err)
    exit(-1)

print('Result: ', divisible / divider)
