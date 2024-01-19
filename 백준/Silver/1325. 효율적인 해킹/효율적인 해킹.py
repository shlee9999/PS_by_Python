from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
next = [[] for _ in range(n+1)]
count = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    next[b].append(a)


cnt = 0
max_cnt = 0
res = []


def bfs(node):
    global max_cnt, res
    cnt = 0
    q = deque()
    visited = [False] * (n+1)
    q.append(node)
    visited[node] = True
    while q:
        cnt += 1
        cur_node = q.popleft()
        for x in next[cur_node]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    # print(node,cnt, end=", ")
    if cnt > max_cnt:
        max_cnt=cnt
        res = [node]
    elif cnt == max_cnt:
        res.append(node)


for start in range(1, n+1):
    bfs(start)

print(*res)
