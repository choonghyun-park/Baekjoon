import sys
T = int(input())
la = []
lb = []
for i in range(T):
    A,B = sys.stdin.readline().rstrip().split()
    A = int(A)
    B = int(B)
    la.append(A)
    lb.append(B)

for i in range(T):
    print("Case #"+str(i+1)+": "+str(la[i])+" + "+str(lb[i])+" = "+str(la[i]+lb[i]))

    