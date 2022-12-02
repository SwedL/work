



from itertools import starmap


def roundrobin(*args):
    list1 = []
    #list2 =
    # for i in args:
    #     starmap(lambda k: list1.append(k), list(enumerate(i)))
    #     print([enumerate(i)])
    #     # for k in enumerate(i):
    #     #     list1.append(k)
    [list1.append(k) for k in enumerate(i for i in args)]
    list1.sort(key=lambda x: x[0])
    print(list1)
    return starmap(lambda n, c: c, list1)




print(*roundrobin('abc', 'd', 'ef'))

numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))

print(list(roundrobin()))