T = int(input())
lst_R = []
lst_S = []
for i in range(T):
    R,S = input().split()
    lst_R.append(int(R))
    lst_S.append(S)

for i in range(len(lst_R)):
    string = lst_S[i]
    iterate = lst_R[i]
    for s in string:
        for _ in range(iterate):
            print(s,end='')
    print()

