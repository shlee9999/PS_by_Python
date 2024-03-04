import sys

input = sys.stdin.readline
V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
edges = []
for _ in range(E):
    v, e, cost = map(int, input().split())
    edges.append((cost, v, e))
edges.sort()


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a = parent[a]
    b = parent[b]
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


res = 0
for edge in edges:
    cost, v, e = edge
    if find_parent(v) != find_parent(e):
        union_parent(v, e)
        res += cost

print(res)
