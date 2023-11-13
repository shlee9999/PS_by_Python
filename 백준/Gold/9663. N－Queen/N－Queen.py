import sys

input = sys.stdin.readline
n = int(input())

blocked1 = [0] * n  # y좌표 확인
blocked2 = [0] * (2 * n - 1)  # x+y 확인
blocked3 = [0] * (2 * n - 1)  # x-y 확인


def is_blocked(x, y):
    if blocked1[y] or blocked2[x + y] or blocked3[x - y + n - 1]:
        return 1
    return 0


def block(x, y):
    blocked1[y] = 1
    blocked2[x + y] = 1
    blocked3[x - y + n - 1] = 1


def unblock(x, y):
    blocked1[y] = 0
    blocked2[x + y] = 0
    blocked3[x - y + n - 1] = 0


result = 0


def func(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        if not is_blocked(x, i):
            block(x, i)
            func(x + 1)
            unblock(x, i)


func(0)
print(result)
