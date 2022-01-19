T = int(input())
def checkIncrease(num):
    for i in range(1, len(num)):
        if num[i] <= num[i-1]:
            return False
    return True

def checkDecrease(num):
    for i in range(1, len(num)):
        if num[i] >= num[i-1]:
            return False
    return True
while T > 0:
    n = input()
    check = False
    if len(n) < 3:
        print("NO")
    else:
        for i in range(0, len(n)):
            if checkIncrease(n[0:i+1]) and checkDecrease(n[i:len(n)]):
                check = True
                break
        if check == False:
            print("NO")
        else:
            print("YES")


    T -= 1