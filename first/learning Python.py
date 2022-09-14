
import sys

data = list(map(int, map(str.strip, sys.stdin)))
for player in data[::-1]:
    if player % 2 == 0:
        print(['Арни', 'Дима'][data.index(player)%2 == 0])
        break