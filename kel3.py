list = [i for i in range(50) if i % 2 !=0]
div_3 = filter(lambda num: num % 3 == 0, list)
print(tuple(div_3))
