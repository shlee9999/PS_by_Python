num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
res = [num1[0] * num2[1] + num2[0] * num1[1], num1[1] * num2[1]]
for i in range(min(res), 0, -1):
    if res[0]%i == 0 and res[1]%i ==0:
        print(res[0]//i, res[1]//i)
        break


