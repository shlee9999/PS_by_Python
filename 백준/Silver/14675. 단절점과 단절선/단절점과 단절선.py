import sys

input = sys.stdin.readline

N = int(input())

link = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:  # 단절점?
        if len(link[k]) > 1:
            print("yes")
        else:
            print("no")
    if t == 2:  # 단절선?
        print("yes")
