n = 3
res = []
while n > 0:
    res.append(int(input()))
    n -= 1
ans = sorted(res)
for i in ans:
    print(i)