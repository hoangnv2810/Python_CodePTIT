hang = int(input())
cot = int(input())

if hang%2 != 0 and cot%2 != 0:
    print("YES")
elif hang%2 != 0 and cot%2 == 0:
    print("NO")
elif hang%2 == 0 and cot%2 == 0:
    print("YES")
else:
    print("NO")