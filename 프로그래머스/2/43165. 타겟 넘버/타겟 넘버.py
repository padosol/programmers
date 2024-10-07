answer = 0

def solution(numbers, target):

    dfs(numbers, 0, target, 0)

    return answer


def dfs(numbers, depth, target, sum):
    if depth == len(numbers):
        if sum == target:
            global answer
            answer += 1
    else:
        dfs(numbers, depth + 1, target, sum + numbers[depth])
        dfs(numbers, depth + 1, target, sum - numbers[depth])