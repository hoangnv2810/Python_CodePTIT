a, K, N = [int(x) for x in input().split()]
res = []

i = 1
while i <= N/K:
    if i*K-a > 0:
        res.append(i*K-a)
    i += 1

if len(res) == 0:
    print(-1)
else:
    for i in res:
        print(i, end=" ")