a, b = input().split()
a=int(a)
b=int(b)

answer = None
if a>b: answer=">"
elif a<b: answer="<"
else: answer="=="

print(answer)
