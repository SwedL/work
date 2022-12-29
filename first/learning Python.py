

import re


x, y = [int(i) for i in input().split(' ')]
rejex_obj = re.compile(r'\d+')
result = sum(map(int, rejex_obj.findall(input(), pos=x, endpos=y)))
print(result)
