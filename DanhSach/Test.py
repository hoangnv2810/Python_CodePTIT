# n, m = map(int, input().strip().split())
# print(n, m)
dp = ["" for i in range(94)]
dp[1] = "0"
dp[2] = "1"
for i in range(3, 7):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[6])