def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
res = [num1[0] * num2[1] + num2[0] * num1[1], num1[1] * num2[1]]
G = gcd(res[0], res[1])
print(res[0] // G, res[1] // G)

