import sys
a = [False, False] + [True] * 1000000
for i in range(1001):
    if a[i]:
        for j in range(i * 2, 1000000, i):
            a[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    for i in range(3, 1000000, 2):
        if a[i] and a[n-i]:
            print(n, '=', i, '+', n-i)
            break
    else:
        print('Goldbach\'s conjecture is wrong.')
