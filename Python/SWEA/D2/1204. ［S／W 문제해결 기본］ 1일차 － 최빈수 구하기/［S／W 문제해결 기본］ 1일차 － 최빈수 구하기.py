from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    scores = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in scores:
        dic[i] += 1
    mode = max(dic.values())
    mode_can = [k for k,v in dic.items() if v==mode]
    print(f"#{num} {max(mode_can)}")