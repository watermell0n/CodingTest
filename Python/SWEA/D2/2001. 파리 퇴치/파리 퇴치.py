T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s_max = 0
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            c_arr = [row[i:i+m] for row in arr[j:j+m]]
            s = sum(sum(row) for row in c_arr)
            if s > s_max:
                s_max = s
    print(f"#{test_case} {s_max}")