visited = []


def solution(n, computers):
    global visited
    visited = [0] * n
    count = 0
    for i in range(n):
        if visited[i] == 1:
            continue
        dfs(n, computers, i)
        count += 1
    return count


def dfs(n, computers, node):
    global visited
    visited[node] = 1
    for i in range(n):
        if visited[i] == 1:
            continue
        if computers[node][i] != 1:  # 연결 X
            continue
        dfs(n, computers, i)
