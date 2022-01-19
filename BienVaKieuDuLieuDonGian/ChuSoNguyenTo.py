import math
def check(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

T = int(input())
while T > 0:
    n = input()
    cnt = 0
    if check(len(n)):
        for i in n:
            if check(int(i)):
                cnt += 1
        if cnt > len(n)-cnt:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    T -= 1