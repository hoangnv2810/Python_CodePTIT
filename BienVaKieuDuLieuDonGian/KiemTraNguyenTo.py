import math

T = int(input())

def check(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
while T > 0:
    s = input()
    if check(int(s[-4:])):
        print("YES")
    else:
        print("NO")
    T -= 1