n,m = map(int, input().split())
arr = list()

for i in range(n):
    arr.append(0)
    
for x in range(m):
    i,j,k = map(int, input().split())
    for y in range(i-1,j):
        arr[y] = k
        
print(' '.join(map(str, arr)))