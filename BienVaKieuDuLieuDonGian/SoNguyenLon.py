import math

T = int(input())
while T > 0:
    a = int(input())
    b = int(input())
    print(math.gcd(a, b))
    T -= 1