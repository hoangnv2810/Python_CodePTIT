def solution(a, n):
    mp = {}
    check = 0
    res = 0
    for i in range(n):
        if a[i] in mp:
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1
    for key in mp:
        if mp[key] > n//2:
            check = 1
            res = key
            break
    if check == 0:
        print("NO")
    else:
        print(res) 

def main():
    T = int(input())
    while T > 0:
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        solution(a, n)
        T -= 1

if __name__ == "__main__":
    main()