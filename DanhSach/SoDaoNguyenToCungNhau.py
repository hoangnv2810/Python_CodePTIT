import math
t = int(input())
while t > 0:
    n = input()
    if math.gcd(int(n), int(n[::-1])) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1