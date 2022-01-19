n = int(input())
a = [[j for j in range(n)] for i in range(n)]
sum = 0
for i in range(n):
    tmp = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = tmp[j]
        sum += a[i][j]
sumA = int(sum/(2*(n-1)))
res = []
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += a[i][j]
    if n == 2:
        res.append(1)
    else:
        res.append(int((tmp-sumA)/(n-2)))

for i in res:
    print(i, end=" ")