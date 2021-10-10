with open('test5.3.txt') as file:
    print(file.readlines())
    file.seek(0)
    sum = 0
    print('Workers with revenue < 20000 / month:')
    for i in file.readlines():
        split_str = i.split(' ')
        split_str[1].replace('\n', '')
        sum += float(split_str[1])
        if float(split_str[1]) < 20000:
            print(split_str[0])
    file.seek(0)
    print('Average revenue of all workers per month is: ', sum / len(file.readlines()))
