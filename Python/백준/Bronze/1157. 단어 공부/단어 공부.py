word = input()
word = [s.upper() for s in word]
alphabet = [0] * 26
maxNum = 0
maxWord = ''

for i in word:
    num = ord(i)-65
    alphabet[num] += 1
    if alphabet[num] > maxNum: 
        maxNum = alphabet[num]
        maxWord = i

same = 0
for j in alphabet:
    if maxNum == j: same += 1
    
print('?' if same >=2 else maxWord)