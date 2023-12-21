import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

if m == 0:
    broken = []
else:
    broken = list(map(int, input().split()))

res = 1000001
diff = abs(res - n)  # 채널 이동 안함

for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
    else:
        if len(num) + abs(int(num) - n) < len(str(res)) + abs(res - n):
            res = int(num)

print(min(len(str(res)) + abs(res - n), abs(100 - n)))
