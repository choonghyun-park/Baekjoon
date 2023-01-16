year = int(input())

anw = 0

if year%400==0:
    anw=1
elif year%4==0 and year%100!=0:
    anw=1
    
print(anw)
