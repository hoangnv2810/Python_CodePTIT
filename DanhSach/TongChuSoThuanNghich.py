t = int(input())
def check(n):
    if len(n) == 1:
        return False
    m = n[::-1]
    if n == m:
        return True
    else:
        return False
while t > 0:
    n = input()
    m = [int(x) for x in list(n)]
    if check(str(sum(m))):
        print("YES")
    else:
        print("NO")

    t -= 1