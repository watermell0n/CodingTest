n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
for x in range(m):
    i, j = map(int, input().split())
    arr[i-1:j] = list(reversed(arr[i-1:j]))
print(' '.join(map(str, arr)))