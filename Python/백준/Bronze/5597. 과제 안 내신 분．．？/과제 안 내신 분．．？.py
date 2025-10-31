arr = [0 for i in range(30)]
for j in range(28):
    n = int(input())
    arr[n-1] = 1
arr2 = list()
for k in range(30):
    if (arr[k]==0):
        arr2.append(k+1)
print(min(arr2))
print(max(arr2))