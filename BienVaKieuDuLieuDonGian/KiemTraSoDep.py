T = int(input())
def check(num):
    if len(set(n)) != 2:
        return False
    for i in range(1, len(num)-1):
        if num[i-1] != num[i+1]:
            return False
    return True
while T > 0:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    T -= 1