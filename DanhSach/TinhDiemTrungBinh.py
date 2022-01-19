n = int(input())
def check(a):
    Min = min(a)
    Max = max(a)
    return [x for x in a if x != Min and x != Max]
a = [float(x) for x in input().split()]
b = check(a)
print(round(sum(b)/len(b), 2))
