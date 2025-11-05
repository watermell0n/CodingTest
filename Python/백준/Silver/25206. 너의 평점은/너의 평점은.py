import sys
input = sys.stdin.readline

credits = []
stat = [4.0,3.0,2.0,1.0]
s = 0
for i in range(20):
    course, credit, grade = map(str, input().strip().split())
    
    if grade!='P':
        credits.append(float(credit))
        fGrade = 0.0
        
        if (grade!='F'):
            fGrade = stat[ord(grade[0])-65]
            fGrade += 0.5 if (grade[1]=='+') else 0.0
        s += float(credit) * fGrade
    
print(s/sum(credits))