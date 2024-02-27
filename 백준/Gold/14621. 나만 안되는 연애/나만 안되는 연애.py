import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nodes = ['X'] + input().split()
edges = []
parent = [i for i in range(N + 1)]


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    u, v, d = map(int, input().split())
    if nodes[u] != nodes[v]:
        edges.append((d, u, v))

edges.sort()
cost = 0
cnt = 0
for edge in edges:
    d, u, v = edge
    if find_parent(u) != find_parent(v):  # 사이클 X
        union_parent(u, v)
        cost += d
        cnt += 1
if cnt < N-1:
    print(-1)
else:
    print(cost)
