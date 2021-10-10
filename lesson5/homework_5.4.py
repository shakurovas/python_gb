import re

nums_dict = {'One': 'Один',
             'Two': 'Два',
             'Three': 'Три',
             'Four': 'Четыре'}

with open('test5.4.1.txt', 'r+') as file:
    with open('test5.4.2.txt', 'w') as file2:
        for line in file.readlines():
            eng_word = re.match('One|Two|Three|Four', line)
            index = str(eng_word.group(0))
            file2.write(line.replace(index, nums_dict[index]))
