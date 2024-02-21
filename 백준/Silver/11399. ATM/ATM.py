import sys
input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
P.sort()
S = [sum(P[:i+1]) for i in range(N)]
print(sum(S))
