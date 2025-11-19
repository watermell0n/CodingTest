for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    isDone = False
    for i in range(dump):
        maxH = max(arr)
        minH = min(arr)
        if (maxH-minH <=1):
            isDone = True
            break
        else:
            maxI = arr.index(maxH)
            minI = arr.index(minH)
            arr[maxI] -= 1
            arr[minI] += 1
    if (not isDone):
        h = max(arr)-min(arr)
    print(f"#{test_case} {h}")