from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return bfs(0, 0, maps, n, m)


def bfs(x, y, maps, n, m):
    q = deque()
    q.append((x, y))
    graph = [[0] * m for _ in range(n)]
    graph[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0 or graph[nx][ny] != 0 and graph[nx][ny] <= graph[x][y] + 1:
                continue
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

    return graph[n - 1][m - 1] if graph[n - 1][m - 1] != 0 else -1
