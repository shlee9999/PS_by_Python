n = int(input())

dp = [0] * (n + 1)
li = list(map(int, input().split()))
p = [0] + li

for k in range(1, n + 1):
    for i in range(1, k+1):
        dp[k] = max(dp[k], dp[k - i] + p[i])
print(dp[n])
