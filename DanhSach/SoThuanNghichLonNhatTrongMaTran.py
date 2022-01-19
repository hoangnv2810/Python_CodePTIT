import math
m, n = [int(x) for x in input().split()]
a = [[0 for j in range(n)] for i in range(m)]

def isTN(n):
    num = str(n)
    return num == num[::-1] and len(num) > 1

listTN = []
for i in range(m):
    tmp = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = tmp[j]
        if isTN(a[i][j]):
            listTN.append(a[i][j])

if len(listTN) == 0:
    print("NOT FOUND")
else:
    maxPrime = max(listTN)
    print(maxPrime)
    for i in range(m):
        for j in range(n):
            if a[i][j] == maxPrime:
                print(f"Vi tri [{i}][{j}]")