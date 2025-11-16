T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cost = 0
    m = 0
    for i in range(n-1, -1, -1):
        if arr[i] > m:
            m = arr[i]
        else:  # arr[i] <= m
            cost += (m-arr[i])
        
    print(f"#{test_case} {cost}")