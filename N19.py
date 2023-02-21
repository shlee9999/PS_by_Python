from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x1, y1, x2, y2):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.appendleft((y1 - 1, x1 - 1))
    dist = 0
    while q:
        qSize = len(q)
        for z in range(qSize):
            cur = q.pop()
            y = cur[0]
            x = cur[1]
            if y == y2 - 1 and x == x2 - 1:
                return dist
            visited[y][x] = 1
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < N:
                    if not graph[ny][nx] and not visited[ny][nx]:
                        q.appendleft((ny, nx))
        dist += 1
    return -1


N = int(input())
graph = [[0] * N] * N
for i in range(N):
    graph[i] = list(map(int, input().split()))  # 이차원 배열 입력
T = int(input())
result = 0
for i in range(T):
    a, b, c, d, ans = map(int, input().split())
    if bfs(a, b, c, d) == ans:
        result += int(100 / T)
print("#total score =", result)
