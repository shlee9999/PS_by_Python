import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

ranges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

enum_list = [num_list[0]]

for i in range(1, n):
    enum_list.append(enum_list[i - 1] + num_list[i])

for r in ranges:
    left = r[0] - 1
    right = r[1] - 1
    if left == 0:
        print(enum_list[right])
    else:
        print(enum_list[right]-enum_list[left-1])