class Country:
    r = 0

    def __init__(self, num, gold, silver, bronze):
        self.num = num
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def rank(self, num):
        self.r = num


N, K = map(int, input().split())
countries = [Country(0, 0, 0, 0)]

for i in range(1, N + 1):
    li = list(map(int, input().split()))
    countries.append(Country(li[0], li[1], li[2], li[3]))
sorted(countries, key=lambda x: (-x.gold, -x.silver, -x.bronze))

cnt = 0
i = 1
while (i <= N):
    cnt += 1
    if i < N and countries[i].gold == countries[i + 1].gold and countries[i].silver == countries[i + 1].silver and \
            countries[i].bronze == countries[i + 1].bronze:
        countries[i].rank(cnt)
        countries[i + 1].rank(cnt)
        i += 1

    else:
        countries[i].rank(cnt)
    i += 1
print(countries[K].r)
