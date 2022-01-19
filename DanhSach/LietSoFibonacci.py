def main():
    T = int(input())
    while T > 0:
        temp = [int(x) for x in input().split()]
        a, b = temp[0], temp[1]
        num1 = 1
        num2 = 1
        for i in range(1, b+1):
            if i >= a and i <= b:
                print(num1, end=" ")
            nth = num1+num2
            num1 = num2
            num2 = nth
        print()
        T -= 1
    

if __name__ == "__main__":
    main()