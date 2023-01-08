import sys
T = sys.stdin.readline()
T = int(T)
l = []
for i in range(T):
    A,B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    l.append(A+B)
for i in range(T):
    print(l[i])