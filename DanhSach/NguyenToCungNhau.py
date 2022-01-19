import math
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
def gcd(a, b):
    if(b == 0): return a
    return gcd(b, a%b)
for i in range(0, n):
    for j in range(i+1, n):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j])
        
        

