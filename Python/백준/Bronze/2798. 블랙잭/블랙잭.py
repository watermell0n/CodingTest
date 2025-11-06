n,m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
for i in range(n):
    a = arr[i]
    for j in range(i+1,n):
        b = arr[j]
        for k in range(j+1,n):
            c = arr[k]
            s = a+b+c
            if (s<=m and s>sum):
                sum = s
print(sum)