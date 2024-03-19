import sys
from collections import deque

INF = 100001
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [INF] * INF


def bfs():
    q = deque()
    for i in range(N + 1):
        dp[i] = N - i
        q.append(i)
    while q:
        cur = q.popleft()
        if N < cur + 1 < INF and dp[cur] + 1 < dp[cur + 1]:
            dp[cur + 1] = dp[cur] + 1
            q.append(cur + 1)
        if N < cur - 1 < INF and dp[cur] + 1 < dp[cur - 1]:
            dp[cur - 1] = dp[cur] + 1
            q.append(cur - 1)
        if N < cur * 2 < INF and dp[cur] < dp[cur * 2]:
            dp[cur * 2] = dp[cur]
            q.append(cur * 2)

bfs()
print(dp[K])
