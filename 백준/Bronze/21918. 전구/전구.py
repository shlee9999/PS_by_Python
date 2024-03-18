import sys

input = sys.stdin.readline
N, M = map(int, input().split())
bulbs = [-1] + list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 전구 상태 c로 변경
        bulbs[b] = c
    elif a == 2:  # b번째부터 c번째까지의 전구의 상태 토글.
        bulbs[b:c + 1] = [1 - x for x in bulbs[b:c + 1]]
    elif a == 3:  # b번째부터 c번째까지의 전구를 끈다.
        bulbs[b:c + 1] = [0] * (c - b + 1)
    elif a == 4:  # b번째부터 c번째까지의 전구를 켠다.
        bulbs[b:c + 1] = [1] * (c - b + 1)
print(*bulbs[1:])