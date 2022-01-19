import re

n, k = [int(x) for x in input().split()]
s = ""
while n > 0:
    s += input() + " "
    n -= 1
tmp = re.findall("\w+", s)
for i in range(len(tmp)):
    if type(tmp[i]) == str:
        tmp[i] = tmp[i].lower()

ans = {i : tmp.count(i) for i in set(tmp) if tmp.count(i) >= k}
d = list(ans.items())
print(d)
for i in range(len(d)):
    for j in range(i+1, len(d)):
        if d[i][1] < d[j][1]:
            d[i], d[j] = d[j], d[i]
        if d[i][1] == d[j][1]:
            if d[i][0] > d[j][0]:
                d[i], d[j] = d[j], d[i]

for i in d:
    print(f"{i[0]} {i[1]}")