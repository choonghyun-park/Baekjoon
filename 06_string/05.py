string = input()

CASE_DIFF = ord('a')-ord('A')

alp_dict = {}
for s in string:
    # change lower case to upper case
    if ord(s)>=97 and ord(s)<=122:
        s = chr(ord(s)-CASE_DIFF)
    if s in alp_dict:
        alp_dict[s]+=1
    else:
        alp_dict[s]=1

max = 0
max_alph = ""
repeated = False
for ord in range(ord('A'),ord('Z')+1):
    if chr(ord) in alp_dict:
        if max==alp_dict[chr(ord)]:
            max = alp_dict[chr(ord)]
            repeated = True
        elif max<alp_dict[chr(ord)]:
            max = alp_dict[chr(ord)]
            max_alph = chr(ord)
            repeated = False
if repeated:max_alph="?"
print(max_alph)