import math
n = int(input())
a = [int(x) for x in input().split()]
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
res = {}
for i in a:
    if isPrime(i) and i in res:
        res[i] += 1
    elif isPrime(i) and i not in res:
        res[i] = 1
for key, value in res.items():
    print(f"{key} {value}")
        

