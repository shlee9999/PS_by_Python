import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    s = input().rstrip()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")