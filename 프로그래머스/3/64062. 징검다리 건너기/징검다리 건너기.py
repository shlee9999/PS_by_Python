sequential_zero = []


def is_possible(stones, k, m):
    cnt = 0
    for i in range(len(stones)):
        if stones[i] <= m:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True


def solution(stones, k):
    copy = sorted(stones)
    low = copy[0]
    high = copy[len(copy)-1]
    while low <= high:
        mid = (low + high) // 2
        if is_possible(stones, k, mid):
            low = mid + 1
        else:
            high = mid - 1
    return low
