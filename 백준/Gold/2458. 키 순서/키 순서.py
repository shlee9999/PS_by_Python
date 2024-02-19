n, m = map(int, input().split())
students = [[0] * n for _ in range(n)]
for _ in range(m):
    short, tall = map(int, input().split())
    students[short - 1][tall - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if students[i][k] == 1 and students[k][j] == 1:  # 사실상 키 비교를 할 수 있는 학생들 연결
                students[i][j] = 1

res = 0
for i in range(n):
    check = 0
    for j in range(n):
        check += students[i][j] + students[j][i]
    if check == n-1:
        res += 1

print(res)
