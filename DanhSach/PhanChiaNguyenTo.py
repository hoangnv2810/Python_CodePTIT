import math

n = int(input())
a = [int(x) for x in input().split()]

def isPrime(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
b = sorted(set(a), key=a.index)
check = False
for i in range(len(b)):
    sumBefor = sum(b[i] for i in range(0, i+1))
    sumAfter = sum(b[i] for i in range(i+1, len(b)))
    if isPrime(sumBefor) and isPrime(sumAfter):
        print(i)
        check = True
        break

if check == False:
    print("NOT FOUND")