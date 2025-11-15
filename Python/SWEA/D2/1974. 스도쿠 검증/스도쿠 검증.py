T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for i in range(9):
        if (sum(arr[i]) != 45):
            flag = 0
            break
        s = 0
        for j in range(9):
            s += arr[j][i]
        if (s != 45):
            flag = 0
            break
            
    if (flag==1):
        for x in range(0,9,3):
            if (flag==1):
                for y in range(0,9,3):
                    c_arr = [row[y:y+3] for row in arr[x:x+3]]
                    s = sum(sum(row) for row in c_arr)
                    if (s != 45):
                        flag = 0
                        break
    print(f"#{test_case} {flag}")