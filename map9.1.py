list = [i for i in range(50) if i % 2 !=0]
div_3 = filter(lambda num: num % 3 == 0, list)
mapping = map(lambda y : y*1, div_3)
for map in mapping:
    print(map, "kelipatan 3")
