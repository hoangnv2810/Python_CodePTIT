t = int(input())
def check(n):
    if len(n)%2 == 0 or n[0] == n[1]:
        return False
    for i in range(2, len(n)):
        if i%2 == 0:
            if n[i-2] != n[i]:
                return False
    return True

while t > 0:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1