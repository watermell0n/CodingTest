T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    prefixSum = [[0]*(n+1) for x in range(n+1)]
    s_max = 0
    for i in range(1, n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    
    for x in range(m,n+1):
        for y in range(m,n+1):
            s = prefixSum[x][y] - prefixSum[x-m][y] - prefixSum[x][y-m] + prefixSum[x-m][y-m]
            s_max = max(s_max, s)
            
    print(f"#{test_case} {s_max}")