def main():
    T = int(input())
    while(T > 0):
        str = input()
        if str.endswith("86") == True:
            print("YES")
        else:
            print("NO")
        T-= 1

if __name__ == "__main__":
    main()

