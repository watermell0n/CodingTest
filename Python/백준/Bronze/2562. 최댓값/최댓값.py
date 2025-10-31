arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
"""arr = [int(input()) for i in range(9)]"""
m = max(arr)
print(m)

print(arr.index(m)+1)
