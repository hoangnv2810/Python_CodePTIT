num = input()
def check(num):
    if num.count("6") + num.count("8") != len(num):
        return False
    if num[0] == "8":
        return False
    for i in range(len(num)):
        if num[i] == "8" and num[i-1] != "6" and num[i-1] != "8":
            return False
        if num[i] == "8" and num[i-1] == "8" and num[i-2] != "6" and i > 1:
            return False
    return True


if check(num):
    print("YES")
else:
    print("NO")