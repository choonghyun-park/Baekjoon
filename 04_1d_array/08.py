import sys

def cont_sum(n):
    s = 0
    for i in range(n):
        s += i+1
    return s

N = int(input())

global_cnts = []

for i in range(N):
    flag = False
    local_cnt = 0
    global_cnt = 0
    case = sys.stdin.readline().rstrip()
    for j,c in enumerate(case):
        if not flag and c=="O":
            flag = True
            local_cnt = 1
            if j==len(case)-1:
                global_cnt += cont_sum(local_cnt)
        elif flag and c=="X":
            flag = False
            global_cnt += cont_sum(local_cnt)
        elif flag and c=="O":
            local_cnt += 1
            if j==len(case)-1:
                global_cnt += cont_sum(local_cnt)
        
    global_cnts.append(global_cnt)

for i in range(N):
    print(global_cnts[i])
    
