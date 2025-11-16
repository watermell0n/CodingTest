T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0]*(c+1) for c in range(n)]
    arr[0][0] = 1
    if (n>=2):
        arr[1][0] = 1
        arr[1][1] = 1
    if (n>=3):
        for i in range(2,n):
            for j in range(i+1):
                if (j==0 or j==i):
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f"#{test_case}")
    for r in arr:
        print(*r)