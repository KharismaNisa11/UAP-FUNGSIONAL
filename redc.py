from functools import reduce
list = [3, 9, 15, 21, 27, 33, 39, 45]
sum = reduce(lambda x, y : x + y, list)
print(sum)