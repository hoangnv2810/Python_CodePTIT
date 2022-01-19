def isEvenOdd(str) -> bool:
    sum = 0
    for i in str:
        sum += int(i)
    for i in range(0, len(str)-1):
        if abs(int(str[i+1])-int(str[i])) != 2:
            return False
    if sum%10 != 0:
        return False
    return True

def main():
    T = int(input())
    while T > 0:
        str = input()
        if isEvenOdd(str):
            print("YES")
        else:
            print("NO")   
        T -= 1


if __name__ == "__main__":
    main()