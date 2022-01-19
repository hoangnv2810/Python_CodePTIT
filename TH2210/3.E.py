row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

def check(hang, cot):
    if hang % 2 != 0 and cot % 2 != 0:
        return "YES"
    elif hang % 2 != 0 and cot % 2 == 0:
        return ("NO")
    elif hang % 2 == 0 and cot % 2 == 0:
        return "YES"
    else:
        return ("NO")

if check(row1, col1) == check(row2, col2):
    print("YES")
else:
    print("NO")
