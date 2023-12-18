n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

s = []

visited = [False] * n


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    prev = 0
    for i in range(n):
        if prev != li[i]:  # prev를 이용해 다음에 올 숫자가 이미 확인했던 값이면 패스한다
            prev = li[i]
            s.append(li[i])
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False


dfs()
