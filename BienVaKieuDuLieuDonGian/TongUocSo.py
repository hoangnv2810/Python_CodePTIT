import math
T = int(input())
sum = 0
while T > 0:
    n = int(input())
    i = 2
    while n%2 == 0:
        sum += 2
        n = n/2
    i += 1
    while i <= n:
        while n%i == 0:
            sum += i
            n = n/i
        i += 2
    T -= 1
print(sum)