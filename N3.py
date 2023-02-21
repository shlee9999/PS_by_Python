for tc in range(10):
    N = int(input())
    s = list(map(int, input().split()))
    M = int(input())
    q = input().split()  # String
    for i in range(len(q)):
        if q[i] == "I":  # ok
            x = int(q[i + 1])
            y = int(q[i + 2])
            for j in range(i + y + 2, i + 2, -1):
                s.insert(x, q[j])
        if q[i] == "D":  # ok
            x = int(q[i + 1])
            y = int(q[i + 2])
            for j in range(y):
                if x > len(s): break
                del s[x]
        if q[i] == "A":
            y = int(q[i + 1])
            for j in range(i + 2, i + y + 2):
                s.append(q[j])
    print("#", tc + 1, sep="", end=" ")
    for i in range(min(10, len(s))):
        print(s[i], end=" ")
    print()
