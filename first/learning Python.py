import re
import sys

data = sys.stdin.read()
result = re.sub(r'"{3}[^"]*"{3}\n', '', data)

print(result)
