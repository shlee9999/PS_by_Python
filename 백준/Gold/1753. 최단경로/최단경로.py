import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    # graph[b].append((a,c))


def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, v + 1):
    print(distance[i] if distance[i] != 1e9 else 'INF')
