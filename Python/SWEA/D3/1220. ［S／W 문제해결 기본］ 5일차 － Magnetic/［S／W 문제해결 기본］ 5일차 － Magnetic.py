T = 10
for test_case in range(1, T + 1):
    n = int(input())
    rect = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    ''' 1과 2만 묶일 수 있는 것 찾아 cnt 세기
    for j in range(n):
        prev = 0
        for i in range(n):
            if (rect[i][j] == 1):
                prev = 1
            elif (rect[i][j]==2 and prev==1):
                cnt += 1
                prev = 0
    '''
    
    # 1과 2로만 이루어진 문자열로 만들어 '12' 개수 세기
    for i in range(n):
        cp = [row[i] for row in rect]
        st = ''.join(map(str, cp)).replace('0','')
        cnt += st.count('12')
    print(f"#{test_case} {cnt}")