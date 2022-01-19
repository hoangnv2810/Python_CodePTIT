T = int(input())
cnt = 1
while T > 0:
    a = input()
    b = input()

    if sorted(a) == sorted(b):
        print(f"Test {cnt}: YES")
    else:
        print(f"Test {cnt}: NO")
    cnt += 1
    T -= 1