n = int(input())
num = ['3', '6', '9']
for i in range(1, n+1):
    cnt = 0
    for j in str(i):
        if j in num:
            cnt += 1
    if (not cnt):
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')