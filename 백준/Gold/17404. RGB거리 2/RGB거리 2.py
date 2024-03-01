import sys

input = sys.stdin.readline
N = int(input())
arr = [[0] * 3 for _ in range(N + 1)]
for i in range(1, N + 1):
    arr[i] = list(map(int, input().split()))

signal = ['R', 'G', 'B']

res = 1000 * N
for rgb in range(3):  # 1, N의 색
    dp = [[1000] * 3 for _ in range(N + 1)]
    dp[1][rgb] = arr[1][rgb]
    for i in range(2, N + 1):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + arr[i][j]
    res = min(dp[N][(rgb + 1) % 3], dp[N][(rgb + 2) % 3], res)

print(res)
