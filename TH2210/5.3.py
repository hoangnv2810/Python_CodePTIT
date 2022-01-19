from math import ceil
lst = list(input())
h = ceil(len(lst)/2)
res = lst[h:] + lst[:h]
for i in res:
    print(i,end="")

