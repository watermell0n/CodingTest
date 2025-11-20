T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ans = 0
    m = n//2
    for i in range(n):
        dis = abs(m-i)	# 중간 행과의 거리
        for j in range(dis, n-dis):
            ans += arr[i][j]
    print(f"#{test_case} {ans}")