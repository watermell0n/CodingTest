arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
m = max(arr)
print(m)
print(arr.index(m)+1)