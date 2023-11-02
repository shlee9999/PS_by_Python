import sys
from copy import deepcopy

input = sys.stdin.readline
n = 10
graph = []
for _ in range(n):
    s = input()
    arr = []
    for i in range(n):
        if s[i] == '#':
            arr.append(False)
        else:
            arr.append(True)  # 켜진 전구가 True
    graph.append(arr)
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
result = 101
for ck in range(1 << 10):
    cnt = 0
    arr = deepcopy(graph)
    for i in range(10):  # 1행
        if ck & (1 << i):  # i번째 스위치 누름
            cnt += 1
            for k in range(5):
                x = 0 + dx[k]
                y = i + dy[k]
                if 0 <= x < 10 and 0 <= y < 10:
                    arr[x][y] = not arr[x][y]
    for i in range(1, 10):  # 2행~10행
        for j in range(10):
            if arr[i - 1][j]:
                cnt += 1
                for k in range(5):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < 10 and 0 <= y < 10:
                        arr[x][y] = not arr[x][y]
    for x in arr:
        if True in x:
            break
    else:
        result = min(result, cnt)

print(result if result != 101 else -1)
