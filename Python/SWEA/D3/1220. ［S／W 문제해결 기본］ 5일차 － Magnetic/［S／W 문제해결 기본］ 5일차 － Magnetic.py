T = 10
for test_case in range(1, T + 1):
    n = int(input())
    rect = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for j in range(n):
        prev = 0
        for i in range(n):
            if (rect[i][j] == 1):
                prev = 1
            elif (rect[i][j]==2 and prev==1):
                cnt += 1
                prev = 0
            
    print(f"#{test_case} {cnt}")