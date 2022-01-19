import math

def isPrime(n) -> bool:
    if n < 2: 
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def main():
    T = int(input())
    while T > 0:
        n = int(input())
        k = 0
        for i in range(1, n+1):
            if math.gcd(i, n) == 1:
                k += 1      
        if isPrime(k):
            print("YES")
        else:
            print("NO")
        T -= 1

if __name__ == "__main__":
    main()