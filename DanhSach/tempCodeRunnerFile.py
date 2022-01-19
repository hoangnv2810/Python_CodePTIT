.split()]
for i in range(10**(k-1), 10**k-1):
    if math.gcd(n, i) == 1:
        print(i, end=" ")