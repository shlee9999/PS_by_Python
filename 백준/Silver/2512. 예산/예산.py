from bisect import bisect_left

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
budgets.sort()
if sum(budgets) <= m:
    print(max(budgets))
else:
    start = 0
    end = max(budgets)
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for x in budgets:
            sum += min(x, mid)
        if sum > m:
            end = mid - 1
        elif sum <= m:
            start = mid + 1
    print(end)

