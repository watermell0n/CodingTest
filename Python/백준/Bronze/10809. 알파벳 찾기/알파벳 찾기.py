s = input()
x = 'a'
for i in range(26):
    print(s.find(x), end=' ')
    x = chr(ord(x)+1)