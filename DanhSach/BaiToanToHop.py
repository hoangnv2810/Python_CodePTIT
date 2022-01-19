import itertools
n, r = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
res = list(itertools.combinations(list(set(a)), r))
for x in res:
    for i in range(len(x)):
        print(x[i], end=" ")
    print()