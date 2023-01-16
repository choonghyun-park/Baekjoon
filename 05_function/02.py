# print self numbers smaller than n
def self_number(n):
    self_numbers = set()
    for i in range(1,n+1):
        number = i
        if number not in self_numbers:
            print(i)
            while(number <= n):
                number = d(number)
                self_numbers.add(number)

# return d(n)
def d(n):
    num = n
    sum = n
    while(num>0):
        sum += num%10
        num = num//10
    return sum

self_number(10000)