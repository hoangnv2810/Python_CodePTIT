a = int(input())
b = int(input())
c = int(input())
if a != b and a != c and b == c:
    print("1")
elif b != a and b != c and a == c:
    print("2")
elif c != a and c != b and a == b:
    print("3")