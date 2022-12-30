import re


res, n = input(), ''

while n != res:
    n = res
    if re.sub(r' ', r'', res).isdigit():
        res = re.sub(r'(\d+)\s+\1', r'\1', res)
    else:
        res = re.sub(r'\b(\w{2,})\W*\s*\1\b', r'\1', res)

print(res)
#1 1 1 1 1 22 22 22 22 333 333 333 4444



# res, n = input(), ''
#
# while n != res:
#     n = res
#     res = re.sub(r'\b(\w{2,})\W*\s*\1\b', r'\1', res)
#
#
# print(res)
