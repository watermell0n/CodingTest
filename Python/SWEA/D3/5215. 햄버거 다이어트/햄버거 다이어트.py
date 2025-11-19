def dfs(index, score, kal):
    global maxScore
    if (kal>l):
        return
    if (score > maxScore):
        maxScore = score
    for i in range(index, n):
        dfs(i+1, score+dic[i][0], kal+dic[i][1])
        
T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    dic = [list(map(int, input().split())) for _ in range(n)]
    maxScore = 0
    dfs(0,0,0)
    print(f"#{test_case} {maxScore}")