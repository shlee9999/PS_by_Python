import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
for n in range(2, N + 1):
    if n % 2 == 1:
        continue
    dp[n] = 3 * dp[n - 2] + 2 * sum(dp[:n - 2])
print(dp[N])
