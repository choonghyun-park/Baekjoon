import sys

def round_3(f):
    ret = f*1000
    ret = round(ret)
    ret = ret/1000
    return ret

N = int(input())
ratio = []
for i in range(N):
    lst = []
    stdin = sys.stdin.readline().rstrip()
    lst = list(map(int,stdin.split()))
    people = lst[0]
    lst = lst[1:]
    avg = sum(lst)/people
    filteredList = list(filter(lambda x:x>avg,lst))

    ratio.append(len(filteredList)/people*100)

for i in range(len(ratio)):
    print("{:.3f}%".format(ratio[i]))