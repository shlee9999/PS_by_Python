n = int(input())
words = [input() for _ in range(n)]
count = 0
for x in words:
    s = set()
    for i in range(len(x)):
        if i == len(x) - 1:
            if x[i] not in s:
                count += 1
            break
        if x[i] != x[i + 1]:
            if x[i] not in s:
                s.add(x[i])
            else:
                break

print(count)
