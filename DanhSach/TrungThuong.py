t = int(input())
while t > 0:
    n = int(input())
    a = {}
    while n > 0:
        r = int(input())
        if r in a:
            a[r] += 1
        else:
            a[r] = 1
        n -= 1
    res_key = max(dict(sorted(a.items(), key=lambda cmp: (cmp[1], cmp[0]))), key=a.get) #key=lambda cmp: cmp[::-1]
    print(res_key)
    t -= 1