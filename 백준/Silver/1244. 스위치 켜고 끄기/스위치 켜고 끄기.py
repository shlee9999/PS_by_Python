switch_cnt = int(input())  # 스위치 개수
switch_status = list(map(int, input().split()))  # 스위치 상태 배열
student_cnt = int(input())  # 학생 수
for i in range(student_cnt):
    a, b = map(int, input().split())
    if a == 1:  # 남학생
        for j in range(switch_cnt):
            if (j + 1) % b == 0:
                switch_status[j] = 1 if switch_status[j] == 0 else 0
    elif a == 2:  # 여학생
        switch_status[b-1] = 1 if switch_status[b-1] == 0 else 0
        left = b - 2
        right = b
        while left >= 0 and right < switch_cnt:
            if switch_status[left] == switch_status[right]:
                switch_status[left] = 1 if switch_status[left] == 0 else 0
                switch_status[right] = 1 if switch_status[right] == 0 else 0
                left -= 1
                right += 1
            else:
                break

result = list(map(str, switch_status))
for idx, value in enumerate(result, 1):  # idx는 1부터 시작
    print(value, end=' ')
    if idx % 20 == 0:  # 20개마다 줄바꿈
        print()
