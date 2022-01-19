def main():
    T = int(input())
    while T > 0:
        n = input()
        count = 0
        for i in n:
            if i == "4" or i == "7":
                count += 1
        if count == len(n):
            print("YES")
        else:
            print("NO")
        T -= 1

if __name__ == "__main__":
    main()