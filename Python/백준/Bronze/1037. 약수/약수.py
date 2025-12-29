num = int(input())
if (num==1):
    n = int(input())**2
else:  
    arr = list(map(int, input().split()))
    arr.sort()
    n = arr[0]*arr[-1]
print(n)