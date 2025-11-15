T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    num = 0
    
    for i in range(n):
        # 행 계산
        cnt = 0
        for j in range(n):
            if (arr[i][j]):
                cnt += 1
            else:
                if (cnt == k):
                    num += 1
                cnt = 0
        if (cnt == k):	# 행 끝까지 검사한 경우
            num += 1
            
        # 열 계산
        cnt = 0
        for p in range(n):
            if (arr[p][i]):
                cnt += 1
            else:
                if (cnt == k):
                    num += 1
                cnt = 0
        if (cnt == k):	# 열 끝까지 검사한 경우
            num += 1

    print(f"#{test_case} {num}")