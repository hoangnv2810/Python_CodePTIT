t = int(input())
def check(s):
    for i in range(1, len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(s[-i-1])-ord(s[-i])):
            return False
    return True

while t > 0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    t -= 1