t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    for s_ in s:
        print(s_*r, end='')
    print()