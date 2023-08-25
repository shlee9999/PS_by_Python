count = 0


def dfs(numbers, target, index, result):
    if index == len(numbers) - 1:  # 마지막 요소
        global count
        if result + numbers[index] == target:
            count += 1
        if result - numbers[index] == target:
            count += 1
        return
    dfs(numbers, target, index + 1, result + numbers[index])
    dfs(numbers, target, index + 1, result - numbers[index])


def solution(numbers, target):
    global count
    dfs(numbers, target, 0, 0)
    answer = count
    return answer
