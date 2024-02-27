N = int(input())
if N == 1:
    print("1")
else:
    cnt = 1
    while cnt <= 30:
        if 2 ** cnt == N:
            print("1")
            break
        cnt += 1
    else:
        print("0")
