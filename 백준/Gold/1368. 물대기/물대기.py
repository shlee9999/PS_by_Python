import sys

input = sys.stdin.readline
n = int(input())
w = list(int(input()) for _ in range(n))
p = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
edges = []
for i in range(n):
    for j in range(n):
        if i < j:
            edges.append((p[i][j], i, j))
for i in range(n):
    edges.append((w[i], i, n))
edges.sort()
total_cost = 0


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)
