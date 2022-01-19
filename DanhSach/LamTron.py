def main():
    T = int(input())
    while T > 0:
        T -= 1
        s = input()
        res = "0"
        if len(s) == 1:
            print(s[0])
            continue
        tmp = int(s[len(s)-1])
        for i in reversed(range(len(s)-1)):
            if i > 0:
                res = "0" + res
            if tmp >= 5:
                tmp = int(s[i])+1
            else:
                tmp = int(s[i])
        res = str(tmp)+res
        print(res)

if __name__ == "__main__":
    main()