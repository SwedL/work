
from collections import Counter

with open('D:/pythonzen.txt', encoding='utf-8') as file:
    data = list(file.read().lower())
    counter = Counter(filter(str.isalpha, data))
    [print(f'{k}: {v}') for k, v in sorted(counter.items())]
