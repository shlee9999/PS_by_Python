N = int(input())
b = 1
cnt = 0
while b < 1 << 31:
    if N & b:
        cnt += 1
    b <<= 1
if cnt == 1:
    print(1)
else:
    print(0)
