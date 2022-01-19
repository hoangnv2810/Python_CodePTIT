while True:
    n = int(input())
    if n == 0:
        break
    a = []
    while n > 0:
        tmp = int(input())
        a.append(tmp)
        n -= 1
    if max(a) == min(a):
        print("BANG NHAU")
    else:
        print(min(a), end=" ")
        print(max(a))