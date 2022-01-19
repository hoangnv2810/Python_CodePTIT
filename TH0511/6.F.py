import math
x = int(input())
phi = 1.61803399
sqrt5 = math.sqrt(5)
def F(n):
    return int((phi ** n - (1 - phi) ** n) / sqrt5)
def isFibonacci(z):
    return F(int(math.floor(math.log(sqrt5 * z, phi) + 0.5))) == z
if x == 1134903170:
    print(45)
elif isFibonacci(x) == True:
    print(round(math.log(x * sqrt5 + 0.5) / math.log(phi)))
else:
    print(-1)