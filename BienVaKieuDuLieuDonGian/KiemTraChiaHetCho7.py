T = int(input())
while T > 0:
    n = input()
    cnt = 0
    while int(n)%7 != 0:
        n = str(int(n) + int(n[::-1]))
        cnt += 1
    print(n)
    T -= 1