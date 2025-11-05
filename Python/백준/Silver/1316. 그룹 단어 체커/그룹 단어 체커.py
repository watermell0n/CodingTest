import sys
input = sys.stdin.readline

num = int(input())
count = num

for i in range(num):
    word = input().strip()
    for c in range(len(word)-1):
        if (word[c] == word[c+1]):
            pass
        elif (word[c] in word[c+1:]):
            count -= 1
            break
print(count)

'''
    exist = set()
    prev = ''
    
    for ch in word:
        if (ch != prev):
            if (ch in exist):
                count -= 1
                break
            exist.add(ch)
        prev = ch        
print(count)'''