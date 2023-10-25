import sys

input = sys.stdin.readline
p, k = map(int, input().split())
a = [False, False] + [True] * (k - 1)
primes = []
for i in range(k):
    if a[i]:
        primes.append(i)
        for j in range(i, k, i):
            a[j] = False

for i in range(len(primes)):
    if p % primes[i] == 0:
        print('BAD', min(primes[i], p//primes[i]))
        break
else:
    print('GOOD')
