T = int(input())
while T > 0:
    s = input()
    if s.count('0') + s.count('1') + s.count('2') != len(s):
        print("NO")
    else:
        print("YES")
    T -= 1