m, n = [int(x) for x in input().split()]
a = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    tmp = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = tmp[j]

col1, col2 = [int(x) for x in input().split()]

for i in range(m):
    for j in range(n):
        if j == col1:
            tmp = a[i][j]
            a[i][j] = a[i][col2]
            a[i][col2] = tmp

for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()