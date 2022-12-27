

import sys
import re




regex = r'\B(<[a-z]+.*?>)\B'

data = sys.stdin.read()
match = re.findall(regex, data, re.I)
print(match)
regex_k = r'<([a-z]+)\s?'
regex_v = r'\bw+=\B'

for i in match:

    print(re.search(regex_k, i))
    print(re.findall(regex_v, i))


