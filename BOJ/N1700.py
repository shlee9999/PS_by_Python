N, K = map(int, input().split()) #멀티탭 스케줄링
parent = list(map(int, input().split()))
tab = []ㅎ
for i in range(N):
    if parent[i] not in tab:
        tab.append(parent[i])
p = N
cnt = 0
while p < K:
    if parent[p] not in tab:
        if len(tab) < N:
            tab.append(parent[p])
            continue
        max_val = 0
        for i in range(N):
            try:  # 뒤에서 발견되면
                max_val = max(max_val, parent[p:].index(tab[i]))
            except ValueError:  # 없으면
                max_val = -1
                tab.pop(i)
                break
        if max_val != -1:
            tab.remove(parent[p + max_val])
        tab.append(parent[p])
        cnt += 1
    p += 1
print(cnt)
