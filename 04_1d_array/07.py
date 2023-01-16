N = int(input())
grades = list(map(int,input().split()))
max_g = max(grades)
lst = []
for i in range(N):
    lst.append(grades[i]/max_g*100)
print(sum(lst)/N)