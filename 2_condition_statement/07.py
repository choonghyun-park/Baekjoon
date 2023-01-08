a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

cnt = 0
m=0
s=a
if a==b: 
    cnt+=1
    s=a
if b==c: 
    cnt+=1
    s=b
if c==a: 
    cnt+=1
    s=c

if cnt==3:
    m = 10000+s*1000
elif cnt==1:
    m = 1000 + s*100
elif cnt==0:
    s = max([a,b,c])
    m = 100*s
print(m)    
