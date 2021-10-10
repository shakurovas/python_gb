with open('test5.2.txt') as file:
    print(f'This file contains {len(file.readlines())} lines')
    print('Number of symbols in each line: ')
    file.seek(0)
    for num, i in enumerate(file.readlines()):
        print(f'#{num+1}: {len(i)-1}')
