"""while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break"""

import sys

for line in sys.stdin:
    line = line.strip("\n")
    a, b = line.split()
    print(int(a)+int(b))