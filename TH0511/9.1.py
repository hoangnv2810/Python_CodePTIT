a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
res = list(set(a).intersection(b))
for i in sorted(res):
    print(i, end=" ")