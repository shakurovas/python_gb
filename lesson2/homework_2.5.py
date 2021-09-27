my_rating = [7, 5, 3, 3, 2]

new_elem = input('Give a new int element for the rating: ')

try:
    new_elem = int(new_elem)
except ValueError:
    print('This is invalid input!')
    exit(-1)

for elem in my_rating:

    if new_elem < elem and my_rating.index(elem) != len(my_rating) - 1:  # checking if this is not the last element (to know that I don't need to add an element to the end of the list yet)
        continue
    elif new_elem >= elem:
        print(my_rating.index(elem))
        my_rating.insert(my_rating.index(elem), new_elem)
        break
    else:
        my_rating.append(new_elem)
        break

print(my_rating)
