import sys

input = sys.stdin.readline
s = input().rstrip()
li = []
cnt = 0
i = 0
while i < len(s):
    if s[i] == '0':
        if i == 0:
            s = s[1:]
            i -= 1
        elif s[i - 1] == '+' or s[i - 1] == '-' or s[i-1] == '(':
                s = s[:i] + s[i + 1:]
                i -= 1

    if s[i] == '-':
        if cnt % 2 == 0:
            s = s[:i + 1] + '(' + s[i + 1:]
        else:
            s = s[:i] + ')' + s[i:]
        cnt += 1
    i += 1
if cnt % 2 == 1:
    s += ')'

print(eval(s))
