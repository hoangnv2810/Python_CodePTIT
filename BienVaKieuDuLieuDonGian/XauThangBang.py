T = int(input())
def check(s):
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(s[len(s)-1-i])-ord(s[len(s)-i-2])):
            return False
    return True

while T > 0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    T -= 1