from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
quantity = [0] * (n + 1)
res = 0
dp = [0] * (n+1)
for end in range(1, n + 1):
    sp = list(map(int, input().split()))
    quantity[end] = sp[0]
    for i in range(2, len(sp)):
        graph[sp[i]].append(end)
        indegree[end] += 1


def topological_sort():
    global res
    q = deque()
    li = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            li.append(quantity[i])
            dp[i] = quantity[i]
    if len(li) > 0:
        res += max(li)
    while q:
        l = len(q)
        tmp = []
        for _ in range(l):
            node = q.popleft()
            for x in graph[node]:
                indegree[x] -= 1
                dp[x] = max(dp[node]+quantity[x], dp[x])
                if indegree[x] == 0:
                    q.append(x)
                    tmp.append(quantity[x])



    print(max(dp))


topological_sort()
