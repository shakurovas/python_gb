def exp(base, pow):
    try:
        base = float(base)
        pow = int(pow)
        base ** abs(pow)
    except TypeError:
        print('Base or/and pow is/are incorrect! Please, check and retry')
        exit(-1)
    result = 1
    for i in range(abs(pow)):
        result = result / base
    return result


base = input('Give a real positive number, please: ')
pow = input('Give an integer negative number, please: ')

if int(base) <= 0 or int(pow) >= 0:
    print('Pow should be < 0, base > 0')
    exit(-1)
print(exp(base, pow))