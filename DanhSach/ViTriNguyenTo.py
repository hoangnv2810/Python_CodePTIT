import math
t = int(input())
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def check(m):
    for i in range(0, len(m)):
        if isPrime(i) and isPrime(m[i]) == False:
            return False
        elif isPrime(i) == False and isPrime(m[i]) == True:
            return False
    return True

while t > 0:
    n = input()
    m = [int(x) for x in list(n)]
    if check(m):
        print("YES")
    else:
        print("NO")
    t -= 1