def sumDigit(x):
    return sum(int(i) for i in str(x))

T = int(input())
while T > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(i+1, n):
            if sumDigit(a[i]) > sumDigit(a[j]):
                a[i], a[j] = a[j], a[i]
            if sumDigit(a[i]) == sumDigit(a[j]) and a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    for i in a:
        print(i, end=" ")
    print()
    T -= 1