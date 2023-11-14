import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
INF = 100001
arr = [INF] * 100001


def func():
    q = deque()
    q.append(n)
    arr[n] = 0
    while q:
        cur = q.popleft()
        if cur == k:
            print(arr[cur])
            sys.exit()

        if 0 <= cur + 1 < INF and arr[cur] + 1 < arr[cur + 1]:
            arr[cur + 1] = arr[cur] + 1
            q.append(cur + 1)
        if 0 <= cur - 1 < INF and arr[cur] + 1 < arr[cur - 1]:
            arr[cur - 1] = arr[cur] + 1
            q.append(cur - 1)
        if 0 <= cur * 2  < INF and arr[cur] + 1 < arr[cur * 2]:
            arr[cur * 2] = arr[cur] + 1
            q.append(cur * 2)


func()
