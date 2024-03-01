import sys

input = sys.stdin.readline
N = int(input())
d = dict()
for _ in range(N):
    s = input().rstrip()
    d.setdefault(s[0], 0)
    d[s[0]] += 1
sorted_dict = sorted(d.items(), key=lambda item: item[0])
if d[max(d, key=d.get)] < 5:
    print("PREDAJA")
else:
    for k, v in sorted_dict:
        if v >= 5:
            print(k, end="")

