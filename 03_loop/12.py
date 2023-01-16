N_org = int(input())
N = N_org
cnt =1
while(1):
    N_1 = N//10
    N_2 = N%10
    sum = N_1 + N_2
    D_1 = N_2
    D_2 = sum%10
    N = 10*D_1+D_2
    if N == N_org:
        break
    else:
        cnt+=1
print(cnt)
