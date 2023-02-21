N, L = map(int, input().split())
arr = list(map(int, input().split()))
leak = [0] * (1001 + L)
for i in arr:
    leak[i] = 1
l = r = 1
length = 0
result = 0
while r <= 1000 + L:
    if leak[r] == 1:
        l = r
        r += L
        result += 1
    else:
        r += 1
print(int(result), end="")
