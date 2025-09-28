def solution(info, edges):
    answer = 0
    visited = [False] * len(info)

    def dfs(sheep, wolf):
        nonlocal answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return

        for l, r in edges:
            if visited[l] and not visited[r]:
                visited[r] = True
                if info[r] == 1:
                    dfs(sheep, wolf + 1)
                else:
                    dfs(sheep + 1, wolf)
                visited[r] = False

    visited[0] = True
    dfs(1, 0)

    return answer