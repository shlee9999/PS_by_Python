import sys


def solution(n, m, x, y, r, c, k):
    result = ''
    dx = r - x
    dy = c - y
    cnt = 0
    if dx > 0:  # down
        for _ in range(dx):
            result += 'd'
            cnt += 1
            if cnt == k:
                return result
    if dy < 0:  # left
        for _ in range(-dy):
            result += 'l'
            cnt += 1
            if cnt == k:
                return result
    if dy > 0:  # right
        for _ in range(dy):
            result += 'r'
            cnt += 1
            if cnt == k:
                return result
    if dx < 0:  # up
        for _ in range(-dx):
            result += 'u'
            cnt += 1
            if cnt == k:
                return result
    # 도착 완료
    if (k - cnt) % 2 == 1:
        return 'impossible'

    if r != n:
        for _ in range(cnt//2):
            result += 'du'
    elif c != m:
        for _ in range(cnt//2):
            result += 'rl'
    return result
