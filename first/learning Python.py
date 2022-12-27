

import sys
import re

regex_teg_with_atr = r'\B(<[a-z]+.*?>)\B'

data = sys.stdin.read()
match = re.findall(regex_teg_with_atr, data, re.I)

regex_teg = r'<([a-z]+)\s?'
regex_atr = r'\b(([a-z]+-?)+)='
dict_res = {}

for i in sorted(match):
   # print(i)
    teg = re.findall(regex_teg, i)[0]
    atr = re.findall(regex_atr, i)
    dict_res[teg] = []
    for k in atr:
        print(teg, k)
        dict_res[teg] = dict_res.get(teg) + [list(k)[0]]

print(dict_res)
# for k, v in dict_res.items():
#     print(f'{k}:', ', '.join(sorted(dict.fromkeys(v))))


