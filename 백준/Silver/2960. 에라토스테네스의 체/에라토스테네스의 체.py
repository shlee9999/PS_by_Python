n, k = map(int, input().split())
arr = [i for i in range(n + 1)]
cnt = 0
result = -1
for i in range(n + 1):
    if i == 0 or i == 1:
        continue
    if arr[i]:
        p = arr[i]
        for j in range(p, n + 1, p):
            if not arr[j]:
                continue
            cnt += 1
            if cnt == k:
                result = arr[j]
                break
            arr[j] = 0
        if cnt == k:
            break

print(result)
