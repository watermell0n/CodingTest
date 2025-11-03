find = list(map(int, input().split()))
white = [1,1,2,2,2,8]
result = [0,0,0,0,0,0]
for i in range(len(white)):
    result[i] = white[i] - find[i]
print(' '.join(map(str, result)))