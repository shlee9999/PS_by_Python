import copy
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
question_list = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * (n) for _ in range(n)]


for l in range(n): #l은 숫자의 길이 -1
    for left in range(n-l): # 0 ~ 숫자의 길이-1 까지
        right = left + l
        if left == right:
            dp[left][right] = 1
        elif arr[left] == arr[right]:
            if left == right - 1:
                dp[left][right] = 1
            elif dp[left+1][right-1] == 1:
                dp[left][right]=1


for q in question_list:
    print(dp[q[0]-1][q[1]-1])
