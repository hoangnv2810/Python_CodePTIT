
def check(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

if __name__ == "__main__":
    num = input()
    if check(num):
        print("YES")
    else:
        print("NO")
