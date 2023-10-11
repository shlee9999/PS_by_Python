from bisect import bisect_left, bisect_right

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()


def get_count(num):
    return bisect_right(arr1, num) - bisect_left(arr1, num)


for x in arr2:
    print(get_count(x), end=' ')
