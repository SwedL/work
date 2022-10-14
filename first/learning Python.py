
from collections import namedtuple

Player = namedtuple('Player', ['A', 'B'])
player = Player(,)

def men_still_standing(cards):
    dict_a = dict([(k, 0) for k in range(1, 12)])
    dict_b = dict([(k, 0) for k in range(1, 12)])
    print(dict_a)
    for i in cards:
        print(i)


men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"])




