import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(start_x, start_y):
    q = deque()
    visited[start_x][start_y] = 1
    q.append((start_x, start_y))
    cnt = 0
    while q:
        cnt += 1
        cur = q.popleft()
        x, y = cur[0], cur[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return cnt


count = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            count += 1
            max_size = max(max_size, bfs(i, j))
print(count)
print(max_size)
