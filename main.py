# Gold 10**12+1~
# Silver 10**6+1~
# Bronze 1~
class Country:
    def __init__(self, num, score):
        self.num = num
        self.score = score


N, K = map(int, input().split())
countries = []

index = -1
for i in range(N):
    li = list(map(int, input().split()))
    countries.append(Country(li[0], li[1] * 10 ** 12 + li[2] * 10 ** 6 + li[3]))
    if li[0] == K:
        index = i
cnt = 0
for i in range(N):
    if countries[i].score > countries[index].score:
        cnt += 1
print(cnt + 1)
