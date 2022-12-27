

import sys
import re

regex_teg_with_atr = r'\B(<[a-z]+.*?>)\B'

data = sys.stdin.read()
match = re.findall(regex_teg_with_atr, data, re.I)

regex_teg = r'<([a-z]+)\s?'
regex_atr = r'\b(([a-z]+-?)+)='
dict_res = {}

for i in sorted(match):
    teg = re.findall(regex_teg, i)[0]
    atr = re.findall(regex_atr, i)
    print(teg, atr)
    dict_res[teg] = dict_res.setdefault(teg, []) + [atr]


# for k, v in dict_res.items():
#     print(f'{k}:', ', '.join(dict.fromkeys(v)))


