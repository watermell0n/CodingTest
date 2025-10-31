arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sum = 0
for i in a:
    for j in arr:
        if (i in j):
            sum += (arr.index(j) + 3)
            break
print(sum)