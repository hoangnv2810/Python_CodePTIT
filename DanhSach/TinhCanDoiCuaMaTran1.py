n = int(input())
a = [[0 for j in range(n)] for j in range(n)]

for i in range(n):
    tmp = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = tmp[j]

k = int(input())
sumA, sumB = 0, 0
for i in range(n):
    for j in range(n):
        if j > i:
            sumA += a[i][j]
        if i > j:
            sumB += a[i][j]
if abs(sumA-sumB) <= k:
    print("YES")
else:
    print("NO")
print(abs(sumA-sumB))