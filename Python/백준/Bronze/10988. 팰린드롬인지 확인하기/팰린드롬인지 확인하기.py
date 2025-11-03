import sys
input = sys.stdin.readline

answer = True
word = input().strip()
for i in range(len(word)//2):
    if (word[i] != word[-(i+1)]):
        answer = False
        break
print(1) if (answer==True) else print(0)