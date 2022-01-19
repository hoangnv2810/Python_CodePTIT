import re

n = int(input())
s = ""
while n > 0:
    s += input() + " "
    n -= 1
a = re.findall("\w+", s)

for i in range(len(a)):
    if type(a[i]) == str:
        a[i] = a[i].lower()

ans = {i : a.count(i) for i in set(a)}
d = list(ans.items())
for i in range(len(d)):
    for j in range(i+1, len(d)):
        if d[i][1] < d[j][1]:
            d[i], d[j] = d[j], d[i]
        elif d[i][1] == d[j][1]:
            if d[i][0] > d[j][0]:
                d[i], d[j] = d[j], d[i]

for i in d:
    print(f"{i[0]} {i[1]}")


