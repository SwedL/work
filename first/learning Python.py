

import sys
import re




regex = r'\B(<[a-z]+.*?>)\B'

data = sys.stdin.read()
match = re.findall(regex, data, re.I)
print(match)




