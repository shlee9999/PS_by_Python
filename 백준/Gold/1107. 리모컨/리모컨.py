import sys

input = sys.stdin.readline
n = int(input())
_str = str(n)
m = int(input())

if m == 0:
    broken = []
else:
    broken = list(map(int, input().split()))

res = 100
usable = [i for i in range(10) if i not in broken]

diff = abs(res - n)  # 채널 이동 안함


def bt(depth, s):
    global res
    if depth == 7 or depth == len(_str) + 2:
        return
    if s != '' and -1 <= depth - len(_str) <= 1:
        res_cnt = len(str(res)) + abs(res - n)
        s_cnt = depth + abs(int(s) - n)
        if res_cnt > s_cnt:  # 더 적게 누르면
            res = int(s)
    for i in range(len(usable)):
        if s == '' and usable[i] == 0:  # 맨 앞자리가 0인 경우는 제외
            res_cnt = len(str(res)) + abs(res - n)
            s_cnt = 1 + n
            if res_cnt > s_cnt:  # 더 적게 누르면
                res = 0
            continue
        bt(depth + 1, s + str(usable[i]))


bt(0, "")
print(min(len(str(res)) + abs(res - n), diff))
