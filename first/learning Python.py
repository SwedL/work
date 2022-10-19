
from collections import Counter


list1 = [len(i) for i in input().lower().split()]
print(list1)
counter = Counter(list1)

print(sorted(counter.items(), key=))
