for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    '''
    for i in range(dump):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1
    print(f"#{test_case} {max(arr)-min(arr)}")
    '''
    
    # 투포인터 알고리즘
    maxH = 100
    freq = [0] * (maxH+1)
    for a in arr:
        freq[a] += 1
        
    l = 0
    while (l<=maxH and freq[l]==0): l+=1
    h = maxH
    while(h>=1 and freq[h]==0): h-=1
    
    for i in range(dump):
        if (h-l)<=1:
            break
        # 1개를 최솟값에서 한 칸 올리기
        freq[l] -= 1
        freq[l+1] += 1
        # 1개를 최댓값에서 한 칸 내리기
        freq[h] -= 1
        freq[h-1] += 1
        while (l<=maxH and freq[l]==0): l+=1
        while(h>=1 and freq[h]==0): h-=1
    
    print(f"#{test_case} {h-l}")