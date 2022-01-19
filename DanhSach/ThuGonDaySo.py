n = int(input())
a = [int(x) for x in input().split()]
i = 1
while i < len(a) and i > 0:
    if (a[i] + a[i-1])%2 == 0:
        a.pop(i)
        a.pop(i-1)
    else:
        i += 1
print(a)
print(len(a))