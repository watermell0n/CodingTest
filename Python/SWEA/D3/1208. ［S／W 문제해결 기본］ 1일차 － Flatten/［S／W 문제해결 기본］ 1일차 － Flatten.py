for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1
    print(f"#{test_case} {max(arr)-min(arr)}")