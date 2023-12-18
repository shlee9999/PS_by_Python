n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if len(s) == 0 or len(s) > 0 and li[i] not in s:
            s.append(li[i])
            dfs()
            s.pop()

dfs()
