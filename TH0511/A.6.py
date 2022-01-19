n = int(input())
res = dict()
for i in range(n):
    k, v = [x for x in input().split(" ", 1)]
    res[k] = v.split(" ")
m = int(input())
ans = []
for i in range(m):
    s = input()
    for k, v in res.items():
        for l in v:
            if s == l:
                ans.append(k)

for i in ans:
    print(i)
