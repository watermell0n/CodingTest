import sys
input = sys.stdin.readline

n = int(input())
result = list(map(int, input().split()))
m = max(result)

for i in range(n):
    result[i] = result[i]/m*100
sum = 0
for j in result:
    sum += j
print(sum/n)