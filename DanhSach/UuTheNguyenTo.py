import math
t = int(input())
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
while t > 0:
    n = input()
    cntPrime = 0
    for i in n:
        if isPrime(int(i)):
            cntPrime += 1
    if isPrime(len(n)) and cntPrime > len(n)-cntPrime:
        print("YES")
    else:
        print("NO")
    t -= 1