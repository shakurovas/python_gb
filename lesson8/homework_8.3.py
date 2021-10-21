class OnlyNums(Exception):
    def __init__(self, txt):
        self.txt = txt


num_elems = []

while True:
    new_elem = input('Give a new elements for your list of numbers here: (if wanna stop, write "stop") ')
    if new_elem == 'stop':
        break
    else:
        try:
            if not new_elem.isdigit():
                raise OnlyNums('Your element should be numeric!')
            else:
                num_elems.append(new_elem)
        except OnlyNums as err:
            print(err)
        print(num_elems)
