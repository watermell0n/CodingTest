n = int(input())
arr = list(map(int, input().split()))
binArr = [bin(a) for a in arr]
lenArr = [0]*22
for a in binArr:
    i = -1
    while (a[i]!='b'):
        if (a[i]=='1'):
            lenArr[i] += 1
        i -= 1
print(max(lenArr))