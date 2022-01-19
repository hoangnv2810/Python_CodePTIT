import functools
def check(s):
    if s >= '0' and s <= '9':
        return False
    return True

def main():
    T = int(input())
    while  T > 0:
        s = input()
        num = 0
        for i in s:
            if check(i) == False:
                num += int(i)
        ans = list(filter(check, s))
        ans.sort()
        string = ""
        for i in ans:
            string += i
        print(string+str(num))
        T -= 1

if __name__ == "__main__":
    main()