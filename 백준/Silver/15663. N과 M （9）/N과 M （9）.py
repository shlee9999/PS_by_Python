n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
new_li = []
for i in range(n):
    if li[i] not in new_li:
        new_li.append(li[i])

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(len(new_li)):
        if len(s) == 0 or len(s) > 0 and s.count(new_li[i]) < li.count(new_li[i]):
            s.append(new_li[i])
            dfs()
            s.pop()


dfs()
