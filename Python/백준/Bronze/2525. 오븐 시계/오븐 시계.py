a, b = map(int, input().split())
c = int(input())
m = a*60 + b + c
if (m >= 1440):
    print(m//60-24, m%60)
else:
    print(m//60, m%60)