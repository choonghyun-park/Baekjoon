def isHansu(n):
    digits = list(map(int,str(n)))
    if len(digits)<=2:
        return True
    diff = digits[0] - digits[1]
    for i in range(1,len(digits)-1):
        tmp = digits[i]-digits[i+1]
        if tmp!=diff:
            return False
    return True

N = int(input())
cnt = 0
for i in range(1,N+1):    
    if isHansu(i):cnt+=1
print(cnt)

