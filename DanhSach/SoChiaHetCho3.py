t = int(input())
import math
def check(n):
    if n%3 == 0:
        return True
    return False
while t > 0:
    n = input()
    m = [int(x) for x in list(n)]
    if check(sum(m)):
        print("YES")
    else:
        print("NO")

    t -= 1