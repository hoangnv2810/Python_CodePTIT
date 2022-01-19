def solve(a, b):
    if a == 0 and b == 0:
        return "VSN"
    elif a == 0:
        return "VN"
    else:
        return -b/a