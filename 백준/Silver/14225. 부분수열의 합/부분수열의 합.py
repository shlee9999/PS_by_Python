import sys

input = sys.stdin.readline
n = int(input())  # n <= 20
s = list(map(int, input().split()))

arr = set()
for i in range(1, 1 << n):
    _sum = 0
    for j in range(n):
        if i & (1 << j):
            _sum += s[j]
    arr.add(_sum)

for i in range(1, sum(s) + 2):
    if i not in arr:
        print(i)
        break
