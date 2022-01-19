n = int(input())
res = {}
for i in range(n):
    k, l = input().split(' - ')
    res[k] = l.split(', ')
ans = {}
print(res)
for k, v in res.items():
    for l in v:
        if l in ans.keys():
            ans[l].append(k)
        else:
            ans[l] = [k]
print(len(ans))
for l, k in sorted(ans.items()):
    print(f"{l} - {', '.join(k)}")