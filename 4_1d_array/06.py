import sys
inputs = []
for _ in range(10):
    input = int(sys.stdin.readline().rstrip())
    namuji  = input%42
    if namuji not in inputs:
        inputs.append(namuji)
print(len(inputs))