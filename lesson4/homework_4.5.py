from functools import reduce

nums_list = [num for num in range(100, 1001) if num % 2 == 0]
print(nums_list)
result = reduce(lambda x, y: x * y, nums_list)
print(result)

