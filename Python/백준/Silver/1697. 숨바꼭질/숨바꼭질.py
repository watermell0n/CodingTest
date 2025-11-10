from collections import deque

n, k = map(int, input().split())
que = deque([n])
time = [0]*100001

while que:
    p = que.popleft()
    if (p==k):
        print(time[p])
        break
    for x in [p-1,p+1,2*p]:
        if (0<=x<=100000 and not time[x]):
            que.append(x)
            time[x] = time[p] + 1