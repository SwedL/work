import re


res, n = input(), ''

res = re.findall(r'(\w+)(\W+)?', res)


print(res)
#1 1 1 1 1 22 22 22 22 333 333 333 4444