T = int(input())
while T > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [0]*n
    for i in range(1, n):
        dp[i] = i
        for j in range(i-1, -1, -1):
            if a[j] <= a[i] and dp[j] != i and j-1 >= 0 and a[i] >= a[j-1]:
                dp[i] = dp[j]
                break
            elif a[j] <= a[i] and dp[j] == i:
                dp[i] = dp[j]
                break

        for l in range(dp[i]-1, -1, -1):
            if a[l] <= a[i]:
                dp[i] = dp[l]
            else:
                break

    for i in range(n):
        print(i-dp[i]+1, end=" ")
    print()
    T -= 1