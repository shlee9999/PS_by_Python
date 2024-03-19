import sys

input = sys.stdin.readline
appoint_list = [[] for _ in range(367)]

N = int(input())
for appoint_idx in range(N):  # 일정 인덱싱
    S, E = map(int, input().split())
    for i in range(S, E + 1):
        appoint_list[i].append(appoint_idx)

res = 0
s = 0
e = 0
h = 0
for date in range(1, 367):
    if len(appoint_list[date]) == 0:  # 일정이 없는 날 -> 넓이 계산
        w = e - s + 1
        area = w * h
        res += area
        # 초기화
        s = 0
        e = 0
        h = 0
    else:  # 일정이 있는 날 -> s == 0, e == 0 이면 새로운 s, e 등록 아니면 e 늘리기
        if s == 0 and e == 0 and h == 0:  # 최초 시도 또는 일정이 없는 날을 거쳐서 옴
            s, e = date, date
            h = 1
        else:
            h = max(h,len(appoint_list[date]))
            e += 1

print(res)
