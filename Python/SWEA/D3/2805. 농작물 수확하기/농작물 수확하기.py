T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    ans = 0
    m = n//2
    ans += sum(int(arr[m][k]) for k in range(n))
    for i in range(1, m+1):
        for j in range(i, n-i):
            ans += int(arr[m-i][j])
            ans += int(arr[m+i][j])
    print(f"#{test_case} {ans}")