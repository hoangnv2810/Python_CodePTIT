import glob

m, n = [int(x) for x in input().split()]
a = [[0 for j in range(n)] for i in range(m)]

def isTN(n):
    num = str(n)
    return num == num[::-1] and len(num) > 1

minMT, maxMT = 10000, -10000
for i in range(m):
    tmp = [int(x) for x in input().split()]
    minMT = min(minMT, min(tmp))
    maxMT = max(maxMT, max(tmp))
    for j in range(n):
        a[i][j] = tmp[j]

num = abs(maxMT-minMT)
res = -1
for i in range(m):
    for j in range(n):
        if a[i][j] == num:
            res = a[i][j]


if res == -1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(m):
        for j in range(n):
            if a[i][j] == num:
                print(f"Vi tri [{i}][{j}]")