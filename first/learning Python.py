import re
import sys

data = sys.stdin.read()
result = re.sub(r'"{3}[^"]*"{3}\n', '', data)
result = re.sub(r'\t*#+ .*\n', '', result)
result = re.sub(r'\s+# .*\n', '\n', result)

print(result)
