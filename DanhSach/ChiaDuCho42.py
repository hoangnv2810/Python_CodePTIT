t = 10
res = []
while t > 0:
    a = input()
    b = [int(x) for x in a.split()]
    t -= len(b)
    for i in b:
        res.append(i%42)
print(len(set(res)))