import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 상어 정보
shark_size = 2
edible_fishes = 0
eaten_fishes = 0

time_count = 0

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start = ()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0
        if graph[i][j] and graph[i][j] < shark_size:
            edible_fishes += 1


# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치


def check_edible_fishes():
    global edible_fishes
    edible_fishes = 0
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < shark_size:
                edible_fishes += 1


def eat_fish(x, y):
    global shark_size, edible_fishes, eaten_fishes
    if 0 < graph[x][y] < shark_size:
        graph[x][y] = 0
        eaten_fishes += 1
        edible_fishes -= 1
        if eaten_fishes == shark_size:
            eaten_fishes = 0
            shark_size += 1
            check_edible_fishes()


def find_shortest_edible_fishes(s):
    global time_count, start, edible_fishes
    if edible_fishes == 0:
        start = (-1, -1)
        return
    visited = [[False] * n for _ in range(n)]
    visited[s[0]][s[1]] = True
    q = deque()
    q.append((s[0], s[1]))
    cnt = 0
    while q:
        if start != s:
            time_count += cnt
            return start
        cnt += 1
        # print('time = ', time_count)
        for k in range(len(q)):
            cur_node = q.popleft()
            # print(cur_node, end=' ')
            x = cur_node[0]
            y = cur_node[1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= shark_size and not visited[nx][ny]:
                    if 0 < graph[nx][ny] < shark_size:  # 잡아 먹을 때
                        if start == s:
                            start = (nx, ny)
                        elif nx < start[0]:  # 위에 있는 물고기
                            start = (nx, ny)
                        elif nx == start[0]:  # 같은 줄에서 왼쪽에 있는 물고기
                            if ny < start[1]:
                                start = (nx, ny)

                        # print()
                    # 0이거나 크기가 같을 때 -> 통과
                    q.append((nx, ny))
                    visited[nx][ny] = True
        # print()
    start = (-1, -1)  # return 안되면 종료
    # print()


while start != (-1, -1):
    find_shortest_edible_fishes(start)
    eat_fish(start[0], start[1])

print(time_count)
