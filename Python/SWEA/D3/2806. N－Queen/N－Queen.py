def dfs(k):
    global answer
    # k:행 번호(하나의 행에 하나의 퀸만 놓을 수 있기 때문)
    if (k==n):	# n개의 퀸을 모두 놓은 경우
        answer += 1
        return
    for i in range(n):
        # i:열 번호
        if (v1[i] == v2[k+i] == v3[k-i+n-1] == 0):
            v1[i]=v2[k+i]=v3[k-i+n-1]=1
            dfs(k+1)
            v1[i]=v2[k+i]=v3[k-i+n-1]=0
            
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [0]*n*n	  # 1차원 배열로
    v1 = [0]*n	 	 # 열 확인 배열
    v2 = [0]*n*2 	# 좌하단우상단 대각선 확인 배열
    v3 = [0]*n*2	# 우하단좌상단 대각선 확인 배열
    answer = 0
    dfs(0)
    print(f"#{test_case} {answer}")