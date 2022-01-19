import math
m, n = [int(x) for x in input().split()]
a = [[0 for j in range(n)] for i in range(m)]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

listPrime = []
for i in range(m):
    tmp = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = tmp[j]
        if isPrime(a[i][j]):
            listPrime.append(a[i][j])

if len(listPrime) == 0:
    print("NOT FOUND")
else:
    maxPrime = max(listPrime)
    print(maxPrime)
    for i in range(m):
        for j in range(n):
            if a[i][j] == maxPrime:
                print(f"Vi tri [{i}][{j}]")