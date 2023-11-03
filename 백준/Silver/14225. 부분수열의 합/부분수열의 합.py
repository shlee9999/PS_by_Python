import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())  # n <= 20
s = list(map(int, input().split()))

arr = set()
for i in range(1, n + 1):
    for c in combinations(s, i):
        arr.add(sum(c))

for i in range(1, max(arr)+ 2):
    if i not in arr:
        print(i)
        break
