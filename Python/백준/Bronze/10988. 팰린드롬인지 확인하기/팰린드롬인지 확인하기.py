import sys
input = sys.stdin.readline

word = input().strip()
print(1) if (word == word[::-1]) else print(0)