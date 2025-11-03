word = input().upper()
alphabet = [0] * 26

for i in word:
    alphabet[ord(i)-65] += 1
    
maxNum = max(alphabet)

n = alphabet.count(maxNum)    
print('?' if n>1 else chr(alphabet.index(maxNum)+65))