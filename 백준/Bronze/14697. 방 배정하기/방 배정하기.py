import sys

input = sys.stdin.readline

a, b, c, n = map(int, input().split())

for i in range(1, n // a + 1):
    for j in range(1, n // b + 1):
        for k in range(1, n // c + 1):
            if a * i + b * j + c * k == n:
                print(1)
                sys.exit()
print(0)
