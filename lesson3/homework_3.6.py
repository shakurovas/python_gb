def int_func(str_line):
    str_line = str_line.split(' ')
    for i in range(len(str_line)):
        if str_line[i].isalpha() and str_line[i].islower():
            str_line[i] = list(str_line[i])
            str_line[i][0] = chr(ord(str_line[i][0]) - 32)
            str_line[i] = ''.join(str_line[i])
        else:
            print('All strings should be in lowercase and do not contain numbers or any other symbols!!!')
            exit(-1)
    print(' '.join(str_line))
    
    
users_str = input('Give any str, please. All letters in lowercase. You can use whitespaces: ')
int_func(users_str)
