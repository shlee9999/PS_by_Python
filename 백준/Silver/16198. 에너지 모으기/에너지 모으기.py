n = int(input())
arr = list(map(int,input().split()))
res = 0
def func(a, E):
    global res
    if len(a) == 2:
        res = max(res, E)
        return
    for i in range(1, len(a)-1):
        func(a[:i]+a[i+1:], E+a[i-1]*a[i+1])

func(arr, 0)
print(res)