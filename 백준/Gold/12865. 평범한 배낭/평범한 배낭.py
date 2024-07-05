import sys

input = sys.stdin.readline

N, K = map(int, input().split())

stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]  # dp[i][j] : 배낭에 넣은 물건 무게의 합이 i 이하일 때 j번 stuff 까지 탐색했을 때의 최대 가치

for i in range(1, N + 1):  # 물건 선택
    weight = stuff[i][0]
    value = stuff[i][1]
    for j in range(1, K + 1):
        if weight > j:  # 아예 들어갈 수 없음
            dp[i][j] = dp[i - 1][j]
        else:  # 현재 물건을 제외한 무게에서 가능한 최대 가치 + 현재 물건의 가치
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])

print(dp[N][K])
