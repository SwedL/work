import random


class Cell:
    def __init__(self, mine, around_mines=0):
        self.mine = random.Random([True, False])
        self.around_mines = around_mines
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = [Cell()]

    def init():
        pass

    def show():
        pass
