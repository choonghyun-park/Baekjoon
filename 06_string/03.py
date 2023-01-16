s = input()

for i in range(ord('a'),ord('z')+1):
    try:
        alphabet = chr(i)
        print(s.index(alphabet),end=' ')
    except:
        print(-1,end=' ')
    

# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('z')-ord('a')) # 25