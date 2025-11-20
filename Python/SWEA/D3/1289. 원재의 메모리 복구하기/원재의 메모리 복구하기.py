T = int(input())
for test_case in range(1, T + 1):
    memory = input()
    ans = 1 if memory[0]=='1' else 0
    for i in range(1,len(memory)):
        if (memory[i] != memory[i-1]):
            ans += 1  
    print(f"#{test_case} {ans}")

    '''
    l = len(memory)
    bit = ['0']*l
    cnt = 0
    prev = 0
    for i in range(l):
        if (memory[i]=='1' and prev==0):
            bit[i:] = '1'*(l-i)
            prev = 1
            cnt += 1
        elif (memory[i]=='0' and prev==1):
            bit[i:] = '0'*(l-i)
            prev = 0
            cnt += 1
    print(f"#{test_case} {cnt}")
    '''