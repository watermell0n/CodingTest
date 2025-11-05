import sys
input = sys.stdin.readline
num = int(input())
for i in range(num):
    word = input()
    exist = []
    while (len(word) > 0):
        if word=='\n': break
        ch = word[0]
        exist.append(ch)
        j = 0
        while (word[j] == ch):
            j += 1
        word = word[j:]
        
    # 중복 문자 검사  
    for ex in exist:
        if (exist.count(ex) > 1):
            num -= 1
            break
print(num)