t = int(input())
while t > 0:
    n = input()
    m = [int(x) for x in list(n)]
    res = 1
    for i in m:
        if i != 0:
            res *= i
    print(res)
    t -= 1