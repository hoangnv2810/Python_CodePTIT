n, m = [int(x) for x in input().split()]
def out(a):
    a.sort()
    for i in a:
        print(i, end=" ")
    print()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
res1 = list(set(a)&set(b))
res2 = [x for x in set(a) if x in a and x not in b]
res3 = [x for x in set(b) if x in b and x not in a]
out(res1)
out(res2)
out(res3)
