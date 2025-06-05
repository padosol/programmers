# n 일, k 근손실
n, k = map(int, input().split())
kit = list(map(int, input().split()))

answer = 0

def dfs(idx, num, weight):
    global answer

    weight += kit[idx]
    weight -= k

    if weight < 500:
        return

    if num == n:
        answer += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i, num + 1, weight)
            visited[i] = False


visited = [False for _ in range(n)]
for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(i, 1, 500)
        visited[i] = False


print(answer)