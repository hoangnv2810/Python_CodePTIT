n = int(input())
res = dict()
while n > 0:
    k, v = [x for x in input().split()]
    v = int(v)
    if k in res.keys():
        res[k] = res[k] + v
    else:
        res[k] = v
    n -= 1



for k in sorted(res.keys()):
    print(k, res[k])