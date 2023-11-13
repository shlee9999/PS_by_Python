import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
INF = 1e9
dist = [[INF] * m for _ in range(n)]
graph = []
q = deque()

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for j in range(m):
        if arr[j] == 1:
            dist[i][j] = 0
            q.append((i, j))


def bfs():
    while q:
        cur = q.popleft()
        x, y = cur[0], cur[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

bfs()
result = 0



for i in range(n):
    for j in range(m):
        if dist[i][j] == INF and graph[i][j] == 0:
            print(-1)
            sys.exit()
        if dist[i][j] != INF:
            result = max(result, dist[i][j])

print(result)
