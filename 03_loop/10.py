import sys
l = []
while(True):
    A,B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    if A==0 and B==0:
        break
    l.append(A+B)

for i in range(len(l)):
    print(l[i])