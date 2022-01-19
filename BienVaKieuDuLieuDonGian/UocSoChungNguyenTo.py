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
        a, b = [int(x) for x in input().strip().split()]
        c = str(math.gcd(a, b))
        res = 0
        for i in c:
            res += int(i)
        if isPrime(res):
            print("YES")
        else:
            print("NO")
        T -= 1


if __name__ == "__main__":
    main()