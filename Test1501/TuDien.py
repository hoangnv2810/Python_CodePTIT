T = int(input())
a = []
while T > 0:
    s = input().split()
    for i in s:
        a.append(i)
    T -= 1

res = {i : round(a.count(i)/len(a), 2) for i in set(a)}
b = list(res.items())
for i in range(len(b)):
    for j in range(i+1, len(b)):
        if b[i][1] < b[j][1]:
            b[i], b[j] = b[j], b[i]
        elif b[i][1] == b[j][1]:
            if b[i][0] > b[j][0]:
                b[i], b[j] = b[j], b[i]

for i in b:
    print(f"{i[0]} {i[1]}")

