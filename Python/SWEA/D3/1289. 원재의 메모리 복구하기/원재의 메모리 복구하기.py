T = int(input())
for test_case in range(1, T + 1):
    memory = input()
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