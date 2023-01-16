import sys
lst = []
for i in range(28):
    stdin = int(sys.stdin.readline().rstrip())
    lst.append(stdin)
lst_no = []
for i in range(30):
    if i+1 not in lst:
        lst_no.append(i+1)
lst_no.sort()
print(lst_no[0])
print(lst_no[1])