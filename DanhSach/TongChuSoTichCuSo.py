t = int(input())
while t > 0:
    n = input()
    cntOld = int(len(n)/2)
    sumEven = 0
    mulOld = 1
    cntZero = 0
    for i in range(0, len(n)):
        if i%2 == 0:
            sumEven += int(n[i])
        elif i%2 == 1 and n[i] != "0":
            mulOld *= int(n[i])
        elif i%2 == 1 and n[i] == "0":
            cntZero += 1
    if cntZero == cntOld:
        mulOld = 0
    print(sumEven, mulOld)
    t -= 1