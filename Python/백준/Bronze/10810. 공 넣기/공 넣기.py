import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [0] * n

for x in range(m):
    i,j,k = map(int, input().split())
    arr[i-1:j] = [k for y in range(j-i+1)]
        
print(' '.join(map(str, arr)))