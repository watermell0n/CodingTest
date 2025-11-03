'''word = input().upper()
alphabet = [0] * 26

for i in word:
    alphabet[ord(i)-65] += 1
    
maxNum = max(alphabet)

n = alphabet.count(maxNum)    
print('?' if n>1 else chr(alphabet.index(maxNum)+65))'''


'''중복 제거하는 집합 자료형 사용'''
word = input().upper()
sWord = list(set(word))
num = []
for ch in sWord:
    num.append(word.count(ch))
cnt = max(num)
if (num.count(cnt) > 1 ):
    print('?')
else:
    print(sWord[num.index(cnt)])
