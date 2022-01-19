import math
t = int(input())
while t > 0:
    n, x, m = [float(x) for x in input().split()]
    print(math.ceil(math.log(m/n, 1+x/100)))
    t -= 1