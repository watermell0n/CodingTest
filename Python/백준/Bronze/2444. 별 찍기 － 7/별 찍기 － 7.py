num = int(input())
for i in range(num):
    print(' '*(num-1-i) + '*'*(2*i+1))
x = 1
for j in range(num-1,0,-1):
    print(' '*x + '*'*(2*j-1))
    x += 1