import re
import sys

data = sys.stdin.read()
match1 = re.findall(r'(<[a-z]+.*?>)', data, re.I)
match2 = re.findall(r'(<[a-z]+>)', data, re.I)

regex_teg = r'<([a-z\d]+)\s?'
regex_atr = r'\b(([a-z]+-?)+)='
dict_res = {}

for i in sorted(match1):
    teg = re.findall(regex_teg, i)[0]
    atr = re.findall(regex_atr, i)
    for k in atr:
        dict_res.setdefault(teg, []).append(list(k)[0])

for i in sorted(match2):
    teg = re.findall(regex_teg, i)[0]
    dict_res.setdefault(teg, [])

for k, v in sorted(dict_res.items()):
    print(f'{k}:', ', '.join(sorted(dict.fromkeys(v))))
