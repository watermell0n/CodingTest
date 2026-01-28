n = int(input())
arr = list(map(int, input().split()))
lenArr = [0]*22
for a in arr:
    i=0
    # a가 0이 되지 않는 동안 반복
    while a:
        if (a&1): lenArr[i]+=1
        a >>= 1
        i+= 1
print(max(lenArr))