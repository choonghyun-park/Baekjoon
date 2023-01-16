X = int(input())
N = int(input())
S = 0
for i in range(N):
    a,b = input().split()
    a = int(a)
    b = int(b)
    S += a*b
if X==S:
    print("Yes")
else:
    print("No")