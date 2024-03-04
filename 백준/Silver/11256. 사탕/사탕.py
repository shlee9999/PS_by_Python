import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    box_list = [list(map(int, input().split())) for _ in range(N)]
    box_list.sort(key=lambda box: -box[0] * box[1])
    res = 0
    for box in box_list:
        box_size = box[0] * box[1]
        J -= box_size
        res += 1
        if J <= 0:
            break
    print(res)
