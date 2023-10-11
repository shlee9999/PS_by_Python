from bisect import bisect_left

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

cards.sort()
for x in arr:
    left = 0
    right = len(cards) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] < x:
            left = mid + 1
        elif cards[mid] > x:
            right = mid - 1
        else:
            result = mid
            break
    if result != -1:
        print(1, end=' ')
    else:
        print(0, end=' ')
