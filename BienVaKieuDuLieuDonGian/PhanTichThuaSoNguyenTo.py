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
        print(f"1", end=" * ")
        for i in range(2, int(math.sqrt(n))+1):
            mu = 0
            if isPrime(i):
                while n%i == 0:
                    mu += 1
                    n = n/i
                if mu != 0 and n != 1:
                    print(f"{i}^{mu}", end = " * ")
                elif mu != 0 and n == 1: 
                    print(f"{i}^{mu}", end = "")
        if n > 1: 
            print(f"{int(n)}^1", end="")
        print()
        T -= 1


if __name__ == "__main__":
    main()