def dfs(k):
    global result	# 함수 안에서 result의 값을 수정하기 위해 global 선언
    if (k==cnt):
        result = max(result, int(''.join(num)))
        return
    for i in range(l-1):
        for j in range(i+1,l):
            num[i], num[j] = num[j], num[i]
            can = int(''.join(num))
            if ((k, can) not in visited):
                visited.append((k,can))
                dfs(k+1)
            num[i], num[j] = num[j], num[i]
            
T = int(input())
for test_case in range(1, T + 1):
    n, cnt = input().split()
    num = list(n)
    l = len(num)
    cnt = int(cnt)
    visited = []
    result = 0
    dfs(0)
    print(f"#{test_case} {result}")