import itertools
res = list(itertools.permutations(list(input())))
print(*[''.join(x) for x in res], sep="\n")


