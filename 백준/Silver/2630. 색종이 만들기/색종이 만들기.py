n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

is_inspected = [[0] * n for _ in range(n)]

res_0 = 0
res_1 = 0


def inspect(l, start_x, start_y):
    global res_0, res_1
    sum = 0
    for i in range(start_x, start_x + l):
        for j in range(start_y, start_y + l):
            if is_inspected[i][j]:
                return 0
            sum += board[i][j]
    if sum == l * l or sum == 0:
        if sum == l * l:
            res_1 += 1
        else:
            res_0 += 1
        for i in range(start_x, start_x + l):
            for j in range(start_y, start_y + l):
                is_inspected[i][j] = 1
        return 1
    return 0


cnt = -1
tmp = n
while tmp > 0:
    tmp //= 2
    cnt += 1

res = 0
for s in range(cnt, -1, -1):
    l = 2 ** s  # 한 변의 길이
    for i in range(0, n, l):
        for j in range(0, n, l):
            inspect(l, i, j)

print(res_0, res_1)
