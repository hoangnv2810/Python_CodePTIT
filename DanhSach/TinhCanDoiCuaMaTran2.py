n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    tmp = [int(x) for x in input().split()]
    for j in range(n):
        a[i][j] = tmp[j]

k = int(input())
sumOn, sumBelow = 0, 0

for i in range(n):
    for j in range(n):
        if j < n-i-1:
            sumOn += a[i][j]
        if j > n-i-1:
            sumBelow += a[i][j]

if abs(sumOn-sumBelow) <= k:
    print("YES")
else:
    print("NO")

print(abs(sumOn-sumBelow))