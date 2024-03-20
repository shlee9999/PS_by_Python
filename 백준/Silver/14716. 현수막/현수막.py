import sys

input = sys.stdin.readline
sys.setrecursionlimit(250 * 250 * 2)

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]


def dfs(x, y):
    board[x][y] = 2
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 1:
            dfs(nx, ny)


res = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1:
            res += 1
            dfs(i, j)

print(res)
