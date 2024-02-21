import sys

input = sys.stdin.readline
N = int(input())
board = [list(input().split()) for _ in range(N)]
cals = ['+', '-', '*']
dx = [0, 1]
dy = [1, 0]

max_ans = -5 ** 13 - 1
min_ans = 5 ** 13 + 1


def dfs(x, y, prev, res):
    new_res = res
    if board[x][y] not in cals:  # 정수
        num = int(board[x][y])
        if prev == '+':
            new_res += num
        if prev == '-':
            new_res -= num
        if prev == '*':
            new_res *= num
        if x == N - 1 and y == N - 1:
            global max_ans, min_ans
            max_ans = max(new_res, max_ans)
            min_ans = min(new_res, min_ans)
            return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, board[x][y], new_res)


dfs(0, 0, '+', 0)

print(max_ans, min_ans)
