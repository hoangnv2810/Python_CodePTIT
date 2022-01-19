import math
def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def main():
    m, n = map(int, input().strip().split())
    a = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        s = list(map(int, input().strip().split()))
        for j in range(n):
            a[i][j] = s[j]
    for i in range(m):
        for j in range(n):
            if(checkPrime(a[i][j]) == True):
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
if __name__ == "__main__":
    main()