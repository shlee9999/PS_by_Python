import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
sub = [(arr[0], 0)] + [0] * (n - 1)
dp = [arr[0]]
for i in range(1, n):
    idx = -1
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        idx = len(dp)-1
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
    sub[i] = (arr[i], idx)

k = len(dp) - 1

result = []
for i in range(n - 1, -1, -1):
    if sub[i][1] == k:
        result.append(sub[i][0])
        k -= 1
print(len(result))
result.reverse()
print(*result)
