a = int(input())
b = int(input())

if a == 0 and b == 0:
    print("many solutions")
elif a == 0 and b != 0:
    print("no solutions")
elif int(b/a) != (b/a):
    print("no solutions")
else:
    print(int(b/a))