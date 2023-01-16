N = int(input())
l = input().split()
v = int(input())
cnt = 0
for i in range(N):
    value = int(l[i])
    if value == v:
        cnt+=1
print(cnt)
