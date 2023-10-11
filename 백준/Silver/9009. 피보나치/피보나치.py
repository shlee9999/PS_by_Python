t = int(input())
tc = [int(input()) for _ in range(t)]

dp = [0] * 51


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n]:
        return dp[n]
    dp[n] = fibo(n - 2) + fibo(n - 1)
    return dp[n]


fibo(50)
enum_list = [dp[0]]

res = [[] for _ in range(t)]
for num, s in enumerate(tc):
    for i in range(50,0,-1):
        if dp[i] > s:
            continue
        if s - dp[i] > 0:
            s -= dp[i]
            res[num].append(dp[i])
        if s - dp[i] == 0:
            res[num].append(dp[i])
            break
for x in res:

    print(' '.join(map(str, sorted(x))))




