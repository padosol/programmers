N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = set([])
visited = [False] * (N + 1)

ans = []
def solve(idx):
    if idx == M:
        answer.add(tuple(ans))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            solve(idx + 1)
            ans.pop()
            visited[i] = False


solve(0)

result = list(answer)
result.sort()
for r in result:
    print(*r)