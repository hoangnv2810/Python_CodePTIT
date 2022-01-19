def main():
    T = int(input())
    while(T > 0):
        str = input()
        res = ""
        temp = ""
        for i in range(0, len(str)):
            if str[i].isdigit():
                res += temp*int(str[i])
                temp = ""
            else:
                temp += str[i]
        print(res)
        T-= 1

if __name__ == "__main__":
    main()