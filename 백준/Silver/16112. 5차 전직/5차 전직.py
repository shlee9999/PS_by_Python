n, k = map(int, input().split())
a = list(map(int, input().split()))  # i번째 퀘스트의 경험치
a.sort()
sum = 0
for i, x in enumerate(a):
    if i == 0:
        continue
    sum += x * min(i, k)

print(sum)
