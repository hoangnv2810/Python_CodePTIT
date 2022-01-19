def SoNhoNhatConThieu(a):
    largest = max(a)
    if largest < 1:
        return 1
    tmp = set(a)
    tmp1 = set(range(1, largest+1))
    res = tmp1-tmp
    if len(res) == 0:
        return largest+1
    else:
        return min(res)

n = int(input())
a = [int(x) for x in input().split()]
print(SoNhoNhatConThieu(a))
