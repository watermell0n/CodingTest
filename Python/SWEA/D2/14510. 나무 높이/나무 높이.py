'''
1,2,1,2,1,2,... 이므로 나무의 키가 자라는 경우를 1과 2로만 나누면 됨
각각의 1과 2의 개수는 나무의 높이 차를 2로 나눈 몫과 나머지 활용하면 됨
나눠서 나온 1과 2를 교차하며 배치한 후, 1 또는 2가 하나 더 남는 경우 그 다음 또는 다다음에 넣어주면 됨
-> 이 법칙을 적용하려면, 1과 2의 각각의 개수 차이가 1을 넘어서는 안 된다.
ex) 1:2개, 2:4개
 1-2-1-2-x-2-x-2 => 8일
 1-2-1-2-1-2-1 => 7일
 이 경우에서, 7일이 소요되는 최소 날짜 수이다.
 즉, 2:1개를 1:2개로 나눠 주는 경우가 최소 날짜 수라는 뜻이다.  
이러한 경우들 때문에 1과 2의 개수 차이가 1로만 되도록 조정해줘야 한다.
번외) 1의 개수 - 2의 개수 > 1 인 경우는 개수 조정을 고려하지 않아도 된다.
 이유: 1을 2로 변경할 수는 없기 때문이다.
  하루에 한 나무에만 물을 줄 수 있다고 명시되어 있으므로, 2개의 나무를 하나로 합쳐 2로 변환할 수 없다.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_tree = max(trees)

    # 1과 2의 개수
    one, two = 0, 0
    for tree in trees:
        if tree == max_tree: continue
        height = max_tree - tree
        two += height // 2
        one += height % 2

    # 1과 2의 개수 차이가 1 또는 0이 되도록 개수 조정
    # -> one==two 이거나, two-one=1 이거나, one>two 인 경우로 나옴
    if two - one > 1:
        while abs(two-one) > 1:
            two -= 1
            one += 2

    # 1과 2의 개수가 같은 경우
    if one == two:
        ans = one + two
    # 2가 1보다 1개 더 많은 경우
    elif two > one:
        ans = 2 * two
    # 1이 2보다 더 많은 경우(몇 개 더 많은지는 모름)
    else:
        ans = 2 * one - 1

    print(f'#{tc} {ans}')