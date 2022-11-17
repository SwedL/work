
from functools import wraps


def takes(*args0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if set(map(lambda x: type(x), (*args, *kwargs.values()))) <= set(args0):
                return func(*args, **kwargs)
            else:
                raise TypeError
        return wrapper
    return decorator


@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))



@takes(str)
def beegeek(word, repeat):
    return word * repeat

try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))

@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))