from collections import deque

q = deque()
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)  # 진입 차수
for _ in range(m):
    node, next = map(int, input().split())
    graph[node].append(next)
    indegree[next] += 1


def topological_sort():
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        print(node, end=' ')
        indegree[node] = -100
        for x in graph[node]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)


topological_sort()
