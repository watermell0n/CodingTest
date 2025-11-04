import sys
input = sys.stdin.readline

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input().strip()

for ch in croatia:
    word = word.replace(ch, '*')
    
print(len(word))