

def get_min_max(iterable):
    if iterable and isinstance(iterable, list):
        return sorted(iterable)[0], sorted(iterable)[-1]
    else:
        try:
            minimum, maximum = next(iterable), max(iterable)
            return minimum, maximum
        except StopIteration:
            pass


iterable = iter([])

print(get_min_max(iterable))


iterable = iter(range(10))

print(get_min_max(iterable))

data = iter(range(100_000_000))

print(get_min_max(data))
iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))
