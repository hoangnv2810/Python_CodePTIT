T = int(input())
while T > 0:
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    # res = list(set(a) & set(b) & set(c))
    # res = [x for x in a if x in b and x in c]
    res = []
    i, j, l = 0, 0, 0
    while i < n and j < m and l < k:
        if a[i] == b[j] and b[j] == c[l]:
            res.append(a[i])
            i += 1
            j += 1
            l += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[l]:
            j += 1
        else:
            l += 1
    if len(res) == 0:
        print("NO")
    else:
        for i in res:
            print(i, end=" ")
        print()
    T -= 1