T = int(input())
a = []
while T > 0:
    s = input().split()
    for i in s:
        a.append(i)
    T -= 1
res = {i: a.count(i) for i in set(a)}

temp = list(res.values())
temp.remove(max(temp))
ans = []
for k, v in res.items():
    if v == max(temp):
       ans.append(k)
ans.sort()
print(*ans)
