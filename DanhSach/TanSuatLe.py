T = int(input())
while T > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    b = set(a)
    for i in b:
        if a.count(i)%2 != 0:
            print(i)
            break
    T -= 1