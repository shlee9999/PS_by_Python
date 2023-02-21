def Hanoi(N, f, t): #N11729
    global k
    if N == 1:
        print(f, t)

        return
    for i in range(1, 4):
        if i != f and i != t:
            mid = i
    Hanoi(N - 1, f, mid)
    print(f, t)
    Hanoi(N - 1, mid, t)


x = int(input())
print(2**x-1)
Hanoi(x, 1, 3)