with open('test5.1.txt', 'w') as file:
    while True:
        text = input('Give here any string, please: ')
        if text == '':
            break
        file.write(text + '\n')
