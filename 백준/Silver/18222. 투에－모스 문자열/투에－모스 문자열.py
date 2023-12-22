n = int(input())


def cal(x, val):
    if x == 0:
        print(val if val == 0 else 1)
        return
    if x % 2 == 0:
        cal(x//2, val)
    else:
        cal(x//2, 1-val)


cal(n-1, 0)
