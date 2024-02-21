import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def align_depth(depth, children, root):  # bfs로 depth 지정
    q = deque()
    q.append(root)  # Root
    d = 0
    while q:
        q_size = len(q)
        for _ in range(q_size):
            cur = q.popleft()
            depth[cur] = d
            for child in children[cur]:
                q.append(child)
        d += 1


def find_common_parent(x, y, depth, parent):
    
    # 항상 y를 더 깊은 depth로
    if depth[x] > depth[y]:
        x, y = y, x
    while depth[x] != depth[y]:  # y의 depth를 x에 맞춰줌
        # print("das")
        y = parent[y]
    # 이제 x, y의 depth가 맞춰짐
    if x == y:  # x가 이미 y의 조상이었던 경우 x를 반환
        return x
    while parent[x] != parent[y]:  # 공통조상 찾기
        x = parent[x]
        y = parent[y]

    return parent[x]


for _ in range(T):
    N = int(input())
    parent = [i for i in range(N + 1)]
    children = [[] for _ in range(N + 1)]
    depth = [0] * (N + 1)
    root = -1
    for _ in range(1, N):  # 간선 N-1개
        p, c = map(int, input().split())
        parent[c] = p
        children[p].append(c)
    for i in range(1, N + 1):
        if parent[i] == i:  # Root
            root = i
    align_depth(depth, children, root)
    a, b = map(int, input().split())
    print(find_common_parent(a, b, depth, parent))
