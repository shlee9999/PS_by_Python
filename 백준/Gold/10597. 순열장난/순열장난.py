import sys

input = sys.stdin.readline

s = input().rstrip()

visited = [False] * 51

res = []


def bt(idx, N, arr):
    if idx >= len(s):
        if False not in visited[1:N + 1]:
            global res
            res = arr
        return
    if idx + 1 < len(s):
        num_1 = int(s[idx:idx + 2]) if int(s[idx:idx + 2]) <= N and not visited[int(s[idx:idx + 2])] else -1
        if num_1 != -1:
            visited[num_1] = True
            bt(idx + 2, N, arr + [num_1])
            visited[num_1] = False
    if idx < len(s):
        num_2 = int(s[idx]) if not visited[int(s[idx])] else -1
        if num_2 != -1:
            visited[num_2] = True
            bt(idx + 1, N, arr + [num_2])
            visited[num_2] = False


if len(s) < 10:  # 한 자릿수
    N = len(s)
    print(' '.join(s))
else:
    N = (len(s) - 9) // 2 + 9
    bt(0, N, [])
    print(*res)
