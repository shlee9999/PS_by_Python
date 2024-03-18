import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000 * 1000 + 1)  # 리미트

M, N = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    board[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
            dfs(nx, ny)


for i in range(N):
    if board[0][i] == 0:
        dfs(0, i)

print("YES" if 2 in board[-1] else "NO")
