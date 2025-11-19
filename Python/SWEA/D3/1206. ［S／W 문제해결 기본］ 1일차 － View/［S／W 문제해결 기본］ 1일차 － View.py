# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(2,n-2):
        leftMax = max(h[i-2], h[i-1])
        leftCnt = (h[i]-leftMax) if (h[i]>leftMax) else 0
        rightMax = max(h[i+2], h[i+1])
        rightCnt = (h[i]-rightMax) if (h[i]>rightMax) else 0
        cnt += min(leftCnt, rightCnt)
    print(f"#{test_case} {cnt}")