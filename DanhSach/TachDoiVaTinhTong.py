num = input()
def sum(a, b):
    return int(a)+int(b)

def solve(n):
    if len(n) == 1:
        return
    a = n[:int(len(n)/2)]
    b = n[int(len(n)/2):]
    print(sum(a, b))
    solve(str(sum(a, b)))

solve(num)