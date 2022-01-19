n, m = [int(x) for x in input().split()]
a = [[0 for j in range(min(m, n))] for i in range(max(n, m))]

for i in range(n):
    tmp = [int(x) for x in input().split()]
    for j in range(m):
        if n > m or n == m:
            a[i][j] = tmp[j]
        else:
            a[j][i] = tmp[j]


res = []
cnt = abs(n-m)
i = 0
while i < max(n, m):
    if cnt > 0:
        if (n > m and i % 2 == 0) or (n < m and i % 2 != 0):
            cnt -= 1
            i += 1
            continue
    res.append(a[i])
    i += 1

for i in range(min(n, m)):
    for j in range(min(n, m)):
        if n > m or n == m:
            print(res[i][j], end=" ")
        else:
            print(res[j][i], end=" ")
    print()
