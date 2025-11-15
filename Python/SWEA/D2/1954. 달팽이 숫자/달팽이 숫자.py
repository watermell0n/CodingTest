T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input()) 
    arr = [[0]*n for _ in range(n)]
    r, c = 0, 0
    # 오, 아, 왼, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    
    for num in range(1, n*n+1):
        arr[r][c] = num
        nx = r + dx[dir]
        ny = c + dy[dir]
        if (nx>=n or nx<0 or ny>=n or ny<0 or arr[nx][ny]!=0):
            dir = (dir+1)%4
            nx = r + dx[dir]
            ny = c + dy[dir]
        r, c = nx, ny
    print(f"#{test_case}")
    for row in arr:
        print(' '.join(map(str, row)))