arr = [0] * 42
for i in range(10):
    n = int(input())
    arr[n%42] = 1
    
count = 0
for j in arr:
    if j==1:
        count += 1
print(count)