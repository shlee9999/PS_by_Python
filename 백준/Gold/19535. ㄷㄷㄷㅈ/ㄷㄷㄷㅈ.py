import math

N = int(input())
connection = [[] for _ in range(N + 1)]
line_li = []
D = 0
G = 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    connection[u].append(v)
    connection[v].append(u)
    line_li.append((u, v))

for i in range(1, N + 1):
    G += math.comb(len(connection[i]), 3)

for line in line_li:
    u, v = line
    D += (len(connection[u]) - 1) * (len(connection[v]) - 1)

if D > G * 3:
    print("D")
elif D < G * 3:
    print("G")
else:
    print("DUDUDUNGA")
