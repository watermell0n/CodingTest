T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for i in range(9):
        s_row = set()
        s_col = set()
        for j in range(9):
            s_row.add(arr[i][j])	# 행 검사
            s_col.add(arr[j][i])	 # 열 검사
        if (len(s_row)!=9 or len(s_col)!=9):
            flag = 0
            break
    # 3x3 검사
    if (flag==1):
        for x in range(0,9,3):
            for y in range(0,9,3):
                block = set()
                for p in range(3):
                    for q in range(3):
                        block.add(arr[x+p][y+q])
                if (len(block) != 9):
                    flag = 0
                    break
            if (flag==0):
                break
    print(f"#{test_case} {flag}")