from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
arr = list(map(str, input().split()))
vowel_num = 0
for i in range(len(vowel)):
    if vowel[i] in arr:
        vowel_num += 1
arr.sort()
combi = list(combinations(arr, L))
for s in range(len(combi)):
    c = 0
    for i in range(len(vowel)):
        if vowel[i] in combi[s]:
            c += 1
    if c >= 1 and L - c >= 2:
        for k in combi[s]:
            print(k, end="")
        if s != len(combi) - 1:
            print()
