import sys

input = sys.stdin.readline
N, K = map(int, input().split())
INF = 100001
dp = [INF] * INF
for i in range(N + 1):  # N 이하는 전부 N - i
    dp[i] = N - i
for i in range(N + 1, INF):
    dp[i] = min(dp[i], dp[i // 2] + i % 2, dp[i - 1] + 1)

for _ in range(10):
    for i in range(N + 1, INF - 1):
        dp[i] = min(dp[i], dp[i // 2] + i % 2, dp[i - 1] + 1, dp[i + 1] + 1)
dp[INF - 1] = min(dp[INF - 2] + 1, dp[INF - 1])

print(dp[K])
