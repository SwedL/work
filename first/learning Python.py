
from itertools import permutations

class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if all(map(lambda y: isinstance(y, (int | float)))) or any(map(lambda x: x <= 0, [self.a, self.b, self.c])):
            return 1
        elif not all(map(lambda x: (x[0] + x[1]) > x[2], permutations([self.a, self.b, self.c]))):
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())














