N,X = map(int,input().split())
l = map(int,input().split())
l = list(l)
l_v = []
cnt = 0
for i in range(N):
    value = l[i]
    if value < X:
        l_v.append(value)
for v in l_v:
    print(v,end=" ")
print()