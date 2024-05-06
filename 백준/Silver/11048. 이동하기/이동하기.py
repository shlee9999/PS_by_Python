import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6 + 1)

N, M = map(int, input().split())

dx = [1, 0, 1]
dy = [0, 1, 1]

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

dp[0][0] = board[0][0]

for i in range(N):
    for j in range(M):
        if i == 0:
            dp[i][j] = dp[i][j - 1] + board[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + board[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + board[i][j]
print(dp[N-1][M-1])
