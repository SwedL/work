
from collections import Counter

data = input().split()
list1 = list(map(lambda x: (x[0], int(x[1])), [[i for i in input().split()] for _ in range(int(input()))]))

list_data = {k: list1[k] for k in data if k in list1}
print(data)
print(list1)
print(list_data)




