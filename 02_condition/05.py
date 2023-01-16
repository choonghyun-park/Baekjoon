H, M = input().split()
H=int(H)
M=int(M)

T = 60*H + M - 45
if T<0:
    T+=60*24
H = T//60
M = T%60
print(H,M)