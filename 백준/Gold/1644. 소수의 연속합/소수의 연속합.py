import sys

input = sys.stdin.readline
n = int(input())
a = [False, False] + [True] * (n - 1)
primes = []
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(i, n + 1, i):
            a[j] = False


if n < 2:
    print(0)
else:
    left, right = 0, 0
    sum = primes[0]
    result = 0
    while left <= right < len(primes):
        if sum > n:
            sum -= primes[left]
            left += 1
        if sum < n:
            right += 1
            if right < len(primes):
                sum += primes[right]
        if sum == n:
            result += 1
            right += 1
            if right < len(primes):
                sum += primes[right]
    print(result)
