import random


class Cell:
    def __init__(self, mine, around_mines=0):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.init()

    def init(self):
        list_res = []
        list1 = [Cell(True) for _ in range(self.M)] + [Cell(False) for _ in range(self.N ** 2)][self.M:]
        random.shuffle(list1)
        for k in range(self.N):
            list_res.append(list1[:self.N])
            list1 = list1[self.N:]
        for i in range(self.N):
            for j in range(self.N):
                for x, y in ([i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]):
                    if 0 <= x <= self.N-1 and 0 <= y <= self.N-1 and list_res[x][y].mine:
                        list_res[i][j].around_mines += 1
        return list_res

    def show(self):
        for i in self.pole:
            print(' '.join([['#', str(k.around_mines)][k.fl_open] for k in i]))

pole_game = GamePole(10, 12)





