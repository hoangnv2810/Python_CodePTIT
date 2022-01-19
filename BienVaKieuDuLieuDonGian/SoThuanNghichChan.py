def isDigitEven(n) -> bool:
    a = str(n)
    if len(a)%2 != 0 or a != a[::-1]:
        return False
    for i in a:
        if(int(i)%2 != 0):
            return False
    return True


def main():
    T = int(input())
    while T > 0:
        n = int(input())
        for i in range(1, n):
            if isDigitEven(i):
                print(i, end=" ")
        print()
        T -= 1

if __name__ == "__main__":
    main()