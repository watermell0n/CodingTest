T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        m, f, a = map(int, input().split())
        total = m*0.35 + f*0.45 + a*0.2
        arr.append(total)
    s_arr = sorted(arr, reverse=True)
    idx = s_arr.index(arr[k-1])
    g = idx//(n//10)
    print(f"#{test_case} {grade[g]}")