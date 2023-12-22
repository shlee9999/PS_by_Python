import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = 50 * 50 + 1
for rangeX in range(n - 7):
    for rangeY in range(m - 7):
        # rangeX~rangeX+7, rangeY~rangeY+7까지 그래프 복사
        g1 = []
        g2 = []
        cnt1 = 0
        cnt2 = 1
        for i in range(rangeX, rangeX + 8):
            g1.append(board[i][rangeY:rangeY + 8])
            g2.append(board[i][rangeY:rangeY + 8])
        g2[0][0] = 'B' if g2[0][0] == 'W' else 'W'
        for x in range(8):
            for y in range(8):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 8 and 0 <= ny < 8 and g1[nx][ny] == g1[x][y]:
                        g1[nx][ny] = 'B' if g1[x][y] == 'W' else 'W'
                        cnt1 += 1
        for x in range(8):
            for y in range(8):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 8 and 0 <= ny < 8 and g2[nx][ny] == g2[x][y]:
                        g2[nx][ny] = 'B' if g2[x][y] == 'W' else 'W'
                        cnt2 += 1

        res = min(res, cnt1, cnt2)
print(res)
