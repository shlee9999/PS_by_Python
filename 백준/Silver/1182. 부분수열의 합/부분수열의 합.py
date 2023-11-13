import sys

input = sys.stdin.readline
n, s = map(int, input().split())
li = list(map(int, input().split()))

result = 0


def func(_sum, x):
    global result
    if x == n:
        if _sum == s:
            result += 1
        return
    func(_sum, x + 1)
    func(_sum + li[x], x + 1)


func(0, 0)
if s == 0:
    result -= 1
print(result)
