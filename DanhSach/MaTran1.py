n = int(input())
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
k = int(input())
totalOver = 0
totalBellow = 0
for i in range(n):
    for j in range(n):
        if j > i:
            totalOver += a[i][j]
        if j < i:
            totalBellow += a[i][j]

if abs(totalOver-totalBellow) < k:
    print("YES")
else:
    print("NO")
print(abs(totalOver-totalBellow))
