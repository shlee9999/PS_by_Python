import sys

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i - 1][j - 1] == 0:
            dp[i][j] = 0
            continue
        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + graph[i - 1][j - 1]
        result = max(result, dp[i][j])

print(result**2)
