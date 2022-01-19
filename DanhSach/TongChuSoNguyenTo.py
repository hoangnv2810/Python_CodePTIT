t = int(input())
import math
def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
while t > 0:
    n = input()
    m = [int(x) for x in list(n)]
    if check(sum(m)):
        print("YES")
    else:
        print("NO")

    t -= 1