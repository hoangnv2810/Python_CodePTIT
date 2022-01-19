m, n = [int(x) for x in input().split()]

for i in range(m):
    for j in range(n):
        if i%2 == 0 and j%2 == 0 or i%2 != 0 and j%2 != 0:
            print(".", end=" ")
        else:
            print("*", end=" ")
    print()