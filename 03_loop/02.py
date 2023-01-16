T = int(input())
l = []
for i in range(T):
    A,B = input().split()
    A = int(A)
    B = int(B)
    l.append(A+B)
for i in range(T):
    print(l[i])
