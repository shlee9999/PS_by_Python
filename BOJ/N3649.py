import sys

while True:
    try:
        n = int(sys.stdin.readline()) * 10000000
        l = int(sys.stdin.readline())
        if l == 0:
            print('danger')
            continue
        elif l == 1:
            sys.stdin.readline()
            print('danger')
            continue
        arr = []
        for i in range(l):
            arr.append(int(sys.stdin.readline()))
        arr.sort()
        left, right = 0, l - 1
        flag = True
        while left < right:
            if arr[left] + arr[right] > n:
                right -= 1
            elif arr[left] + arr[right] < n:
                left += 1
            else:
                print("yes", arr[left], arr[right])
                flag = False
                break
            if left>=right:
                print('danger')
                break
    except:
        break
