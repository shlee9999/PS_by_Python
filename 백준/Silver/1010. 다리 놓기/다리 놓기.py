import math
t = int(input())
arr = [list(map(int,input().split()))for _ in range(t)]
for x in arr:
    nCr = math.comb(x[1], x[0])
    print(nCr)