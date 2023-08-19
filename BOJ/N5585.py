n = int(input())
money = 1000 - n
list = [500, 100, 50, 10, 5, 1]
count = 0
for x in list:
    count += money // x
    money %= x
print(count)
