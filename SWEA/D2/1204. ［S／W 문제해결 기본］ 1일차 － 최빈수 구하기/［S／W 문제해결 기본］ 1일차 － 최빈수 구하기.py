T = int(input())
for _ in range(T):
    t = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res_cnt = 1
    res_num = arr[-1]
    cnt = 1
    for i in range(len(arr)):
        if i == len(arr) - 1: # 마지막 원소
            if res_cnt <= cnt:
                res_cnt = cnt
                res_num = arr[i]
            cnt = 1
        else:
            if arr[i] == arr[i + 1]:
                cnt += 1
            else:
                if res_cnt <= cnt:
                    res_cnt = cnt
                    res_num = arr[i]
                cnt = 1
    print("#", t, sep='', end=' ')
    print(res_num)  # 정답
