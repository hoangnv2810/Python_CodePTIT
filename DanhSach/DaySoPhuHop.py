def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        a.sort(), b.sort()
        check = True
        for i in range(0, n):
            if a[i] > b[i]:
                check = False
                break
        if check == True:
            print("YES")
        else:
            print("NO")
        T -= 1

if __name__ == "__main__":
    main()