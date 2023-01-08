import sys
l = []
while(1):
    try:
        A,B = map(int, sys.stdin.readline().split())
        l.append(A+B)  
    except:
        for i in range(len(l)):
            print(l[i])
        break
