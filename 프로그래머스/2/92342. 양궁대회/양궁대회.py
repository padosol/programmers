import copy

def solution(n, info):
    answer = [-1,0,0,0,0,0,0,0,0,0,0]
    size = 0

    def dfs(n, result, index):
        nonlocal answer
        nonlocal size
        if index < 0:
            return

        if n == 0:
            rion = 0
            apich = 0
            for i in range(11):
                if info[i] < result[i]:
                    rion += (10 - i)
                elif info[i] and info[i] >= result[i]:
                    apich += (10 - i)

            if rion - apich > size:
                size = rion-apich
                if rion > apich:
                    for i in range(10, -1, -1):
                        if answer[i] or result[i]:
                            if answer[i] < result[i]:
                                answer = result
                                break
            return

        # 쏜다
        a = copy.deepcopy(result)
        a[index] += 1
        dfs(n-1, a, index)
        # 안 쏜다.
        b = copy.deepcopy(result)
        dfs(n, b, index - 1)

    result = [0] * 11
    dfs(n, result, 10)

    return [-1] if answer[0] == -1 else answer