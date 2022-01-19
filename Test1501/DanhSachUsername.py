T = int(input())
res = []
while T > 0:
    n = input()
    res.append(n.lower())
    T -= 1
print(*set(res), sep="\n")