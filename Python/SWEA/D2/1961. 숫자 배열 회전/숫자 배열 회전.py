T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]   
    print(f"#{test_case}")
    
    for i in range(n):
        rot_arr = arr
        for t in range(3):
            rot_arr = list(zip(*rot_arr[::-1]))
            for j in range(n):
                print(rot_arr[i][j], end='')
            print(' ', end='')
        print()