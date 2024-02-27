import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    s = input().rstrip()
    if s.count('(') != s.count(')'):
        print("NO")
        continue
    li = []
    for c in s:
        if c == '(':
            li.append(c)
        else:  # c == ')'
            if '(' in li:
                li.remove('(')
            else:  # 실패
                print("NO")
                break
    else:  # 성공
        print("YES")
