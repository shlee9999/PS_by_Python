from itertools import combinations
n, m = map(int, input().split())
li = [i for i in range(1,n+1)]
for c in combinations(li, m):
    print(' '.join(map(str, c)))