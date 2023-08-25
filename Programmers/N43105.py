# 정수 삼각형

def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(n):
            if 1 <= j < len(triangle[i]) - 1:
                dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j], dp[i][j])
            elif j == 0:
                dp[i][j] = max(dp[i - 1][j] + triangle[i][j], dp[i][j])
            elif j == len(triangle[i]) - 1:
                dp[i][j] = max(dp[i - 1][j - 1] + triangle[i][j], dp[i][j])
    answer = max(dp[n - 1])
    return answer
