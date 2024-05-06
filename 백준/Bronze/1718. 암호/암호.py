import sys

input = sys.stdin.readline

sent = input().rstrip()
sec_key = input().rstrip()

ans = ''
for i in range(len(sent)):
    if sent[i] == ' ':
        ans += ' '
    else:
        idx = (ord(sent[i]) - ord(sec_key[i % len(sec_key)])) % 26 + 96
        ans += chr(idx) if idx != 96 else 'z'

print(ans)
