def main():
    while True:
        a = [int(x) for x in input().split()]
        res = 0
        if a[0] == a[1] == a[2] == a[3] == 0:
            break
        while True:
            if a[0] == a[1] == a[2] == a[3]:
                break
            tmp = abs(a[3]-a[0])
            for i in range(0, 3):
                a[i] = abs(a[i]-a[i+1])
            a[3] = tmp
            res += 1
        print(res)

if __name__ == "__main__":
    main()