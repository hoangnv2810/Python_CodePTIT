T = int(input())
while T > 0:
    b = int(input())
    a = input()
    if b == 2:
        print(a)
    elif b == 4:
        print("{0:}")
    elif b == 8:
        print("{0:o}".format())
    T -= 1