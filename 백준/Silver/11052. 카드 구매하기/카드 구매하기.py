n = int(input())
p = [0]
dp = [0] * (n + 1)
li = list(map(int, input().split()))
for i in range(1, n+1):
    dp[i] = li[i-1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j <= n:
            dp[i * j] = max(dp[i] * j, dp[i * j])
        if i + j <= n:
            dp[i + j] = max(dp[i] + dp[j], dp[i + j])
print(dp[n])
