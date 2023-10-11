n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ran = [list(map(int, input().split())) for _ in range(m)]

enum_list = []

for i in range(n):
    li = []
    for j in range(n):
        if j == 0:
            li.append(arr[i][0])
        else:
            li.append(arr[i][j] + li[j - 1])  # 누적 합
    enum_list.append(li)

for r in ran:
    sum = 0
    x1, y1, x2, y2 = r
    left = y1 - 2
    right = y2 - 1
    for i in range(x1 - 1, x2):
        if left == -1:
            sum += enum_list[i][right]
        else:
            sum += enum_list[i][right] - enum_list[i][left]
    print(sum)
