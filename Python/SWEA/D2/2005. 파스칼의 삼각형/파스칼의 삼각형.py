T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0]*(c+1) for c in range(n)]
    
    for i in range(n):
        arr[i][0] = 1
        arr[i][-1] = 1
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f"#{test_case}")
    for r in arr:
        print(*r)