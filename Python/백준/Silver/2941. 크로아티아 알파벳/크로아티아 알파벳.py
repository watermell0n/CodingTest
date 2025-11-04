import sys
input = sys.stdin.readline

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input().strip()
num = 0
for ch in croatia:
    if (ch in word):
        while (word.count(ch) > 0):
            num += 1
            idx = word.find(ch)
            word = word[:idx] + ' ' + word[idx+len(ch):]
word = word.replace(' ','')
for i in word:
    num += 1
print(num)