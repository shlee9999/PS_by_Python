n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
INF = 1e9
dist = [INF] * (n + 1)


def bf(start_node):
    dist[start_node] = 0
    for i in range(1, n + 1):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n:
                    return True  # 사이클 존재
    return False


flag = bf(1)
for i in range(2,n+1):
    if flag:
        print(-1)
        break
    else:
        print(dist[i] if dist[i]<INF else -1)
