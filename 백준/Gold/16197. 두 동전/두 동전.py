import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input() for _ in range(n)]  # m == len(input)
coin = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
INF = 30
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coin.append((i, j))
res = INF


def check(x, y):
    if board[x][y] == 'o' or board[x][y] == '.':
        return 1
    return 0


def bt(x1, y1, x2, y2, depth):
    global res
    if depth > 10:
        return
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if (nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m) and (0 <= nx2 < n and 0 <= ny2 < m) \
                or (nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m) and (
                0 <= nx1 < n and 0 <= ny1 < m):  # 동전 하나만 떨어짐 => clear
            res = min(res, depth + 1)
            return
        if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
            # 둘 다 안 떨어짐 => 이동
            if check(nx1, ny1) and check(nx2, ny2):
                bt(nx1, ny1, nx2, ny2, depth + 1)
            elif check(nx1, ny1) and not check(nx2, ny2):
                bt(nx1, ny1, x2, y2, depth + 1)
            elif not check(nx1, ny1) and check(nx2, ny2):
                bt(x1, y1, nx2, ny2, depth + 1)


bt(coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0)
print(res if res <= 10 else -1)
