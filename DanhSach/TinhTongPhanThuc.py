t = int(input())
while t > 0:
    n = int(input())
    res = 0
    if n%2 == 1:
        for i in range(1, n+1,2):
            res += 1.0/i
    else:
        for i in range(2, n+1, 2):
            res += 1.0/i
    print(format(round(res, 6), '.6f'))
    t -= 1
