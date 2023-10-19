n = int(input())
m = int(input())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))  # a와 b를 연결하는 비용 c
edges.sort()
parent = [i for i in range(n)]
total_cost = 0


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    cost, a, b = edges[i]
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)
