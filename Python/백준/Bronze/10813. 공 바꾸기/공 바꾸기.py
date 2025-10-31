import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [y+1 for y in range(n)]
for x in range(m):
    i, j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
print(' '.join(map(str, arr)))