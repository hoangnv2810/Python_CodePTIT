import math

def phantich(num):
    res = []
    while num%2 == 0:
        res.append(2)
        num /= 2
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num%i == 0:
            res.append(i)
            num /= i
    if num > 1:
        res.append(num)
    return res

def checkMM(num):
    a = phantich(num)
    for i in set(a):
        if num%(i**2) != 0:
            return False
    return True

def checkHH(num):
    ans = 0
    for i in range(1, num):
        if num%i == 0:
            ans += i
    if ans == num:
        return True
    else:
        return False

n = int(input())
if checkMM(n) == True and checkHH(n) == False:
    print("1")
else:
    print("0")