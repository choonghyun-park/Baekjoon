import sys
l = []
for i in range(9):
    stdin = sys.stdin.readline().rstrip()
    l.append(int(stdin))

max = max(l)
index = l.index(max)

print(max)
print(index+1)