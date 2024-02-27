import sys

input = sys.stdin.readline
n = int(input())
dp = [[0] * (n + 1) for _ in range(10)]
for i in range(1, 10):
    dp[i][1] = 1
for j in range(2, n + 1):
    for i in range(10):
        if i == 0:
            dp[i][j] = dp[i + 1][j - 1]
        elif i == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i + 1][j - 1]
result = 0
for i in range(10):
    result += dp[i][n]
print(result % 1000000000)
