n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

b = {i : a.count(i) for i in set(a)}
c = set(list(b.values()))
c.remove(max(c))
if len(c) >= 1:
    maxSecond = max(c)
else:
    maxSecond = -1
ans = sorted(b.items(), key=lambda x: x[1], reverse=True)
if maxSecond == -1:
    print("NONE")
else:
    for key, value in ans:
        if value == maxSecond:
            print(key)
            break