H,M = input().split()
C = int(input())
H = int(H)
M = int(M)

T = 60*H + M + C
if T >= 60*24:
    T -= 60*24

H = T//60
M = T%60
print(H,M)

