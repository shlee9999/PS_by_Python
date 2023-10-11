n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))


def binary_search(num):
    start = 0
    end = len(arr1)-1
    while start <= end:
        mid = (start + end) // 2
        if num > arr1[mid]:
            start = mid + 1
        elif num < arr1[mid]:
            end = mid - 1
        else:
            return 1
    return 0


for x in arr2:
    print(binary_search(x))
