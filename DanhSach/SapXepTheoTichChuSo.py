def mulDigit(x):
    res = 1
    for i in str(x):
        res *= int(i)
    return res

T = int(input())
while T > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(i+1, n):
            if mulDigit(a[i]) > mulDigit(a[j]):
                a[i], a[j] = a[j], a[i]
            if mulDigit(a[i]) == mulDigit(a[j]) and a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    for i in a:
        print(i, end=" ")
    print()
    T -= 1