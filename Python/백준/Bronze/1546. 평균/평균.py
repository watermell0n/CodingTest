import sys
input = sys.stdin.readline

n = int(input())
result = list(map(int, input().split()))
m = max(result)
sum=0
for i in result:
    sum += i/m*100
print(sum/n)