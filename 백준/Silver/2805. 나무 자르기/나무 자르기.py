n, m = list(map(int, input().split()))
array = sorted(list(map(int, input().split())))

start = 0
end = array[-1]

mid = (start + end) // 2
result = -1
while start <= end:
    mid = (start + end) // 2
    l = 0
    for x in array:
        if x > mid:
            l += x - mid
    if m > l:  # 절단기 길이가 길어서 떡이 부족할 때
        end = mid - 1  # 절단기 길이를 늘려 떡이 더 조금 남도록 한다
    else:  # 절단기 길이가 짧아서 딱 맞거나 남는 떡이 많을 때
        result = mid
        start = mid + 1


print(result)
