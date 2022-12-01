



def pairwise(iterable):
    prew = next(iterable)
    for i in iterable:
        yield


numbers = [1, 2, 3, 4, 5]


print(*pairwise(numbers))