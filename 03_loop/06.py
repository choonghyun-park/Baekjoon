import sys
T = int(input())
l = []
for i in range(T):
    A,B = sys.stdin.readline().rstrip().split()
    A = int(A)
    B = int(B)
    l.append(A+B)

for i in range(T):
    print("Case #"+str(i+1)+": "+str(l[i]))

    