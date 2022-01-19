t = int(input())
while t > 0:
    n = input()
    sumOld = 0
    mulEven = 1
    for i in range(0, len(n)):
        if i%2 == 1:
            sumOld += int(n[i])
        elif i%2 == 0 and n[i] != "0":
            mulEven *= int(n[i])
    print(mulEven, sumOld)
    t -= 1