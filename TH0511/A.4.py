n = int(input())
res ={}
list = []
for i in range(n):
    a = [x for x in input().split()]
    for j in a:
        if j not in res:
            res[j] = 0
        res[j] += 1


for k,v in res.items():
    if v == max(res.values()):
        list.append(k)
print(sorted(list)[0])

