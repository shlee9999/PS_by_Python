from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topological_sort(graph, indegree):
    result = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for x in graph[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)
    return result


answer = topological_sort(graph, indegree)
for x in answer:
    print(x, end=' ')
