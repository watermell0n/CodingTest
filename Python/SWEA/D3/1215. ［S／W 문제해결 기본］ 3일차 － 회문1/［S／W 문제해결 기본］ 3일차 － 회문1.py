for test_case in range(1, 11):
    n = 8
    l = int(input())
    arr = [list(input()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        cp_arr = [row[i] for row in arr]  # arr에서 각 열끼리 묶어서 1차원 배열로 추출
        for j in range(n-l+1):
            k = -(n-l-j+1)
            # 행 검사
            if (arr[i][j:j+l] == arr[i][k:k-l:-1]):
                cnt += 1
            # 열 검사
            if (cp_arr[j:j+l] == cp_arr[k:k-l:-1]):
                cnt += 1
    print(f"#{test_case} {cnt}")