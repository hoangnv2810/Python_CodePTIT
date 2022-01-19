def main():
    T = int(input())
    while(T > 0):
        str = input()
        temp = ""
        for i in range(0, 2):
            temp += str[i]
        if str.endswith(temp):
            print("YES")
        else:
            print("NO")
        T-= 1

if __name__ == "__main__":
    main()