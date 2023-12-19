n, m, k = map(int, input().split())
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
res = -1e9
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def check_visited_tile(x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
            return True
    return False



def bt(depth, x, y, s):
    if depth == k:
        global res
        res = max(s, res)
        return
    for i in range(x, n):
        for j in range(m):
            if i == x and j < y:
                continue
            if not visited[i][j] and not check_visited_tile(i, j):
                visited[i][j] = True
                bt(depth + 1, i, j, s + board[i][j])
                visited[i][j] = False   


# for i in range(n):
#     for j in range(m):
#         select_tile(i, j)
#         bt(1, i, j, board[i][j])
#         refresh_tile(i, j)
bt(0,0,0,0)
print(res)
