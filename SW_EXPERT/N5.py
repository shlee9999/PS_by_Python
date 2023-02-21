T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for m in range(M):
        query = input().split()
        if query[0] == "I":
            x = int(query[1])
            y = int(query[2])
            arr.insert(x - 1, y)
        if query[0] == "D":
            del arr[int(query[1])]
        if query[0] == "C":
            x = int(query[1])
            y = int(query[2])
            arr[x] = y
    if L >= len(arr):
        print("#", tc + 1, " -1", sep="")
    else:
        print("#", tc + 1, " ", arr[L], sep="")
