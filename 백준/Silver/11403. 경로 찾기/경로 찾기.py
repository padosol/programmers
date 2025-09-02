from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(start, end, size):
    q = deque()
    q.append(start)

    visited = [False] * size
    visited[start] = True
    while q:
        next = q.popleft()

        for n in graph[next]:
            if n == end:
                return True

            if visited[n]:
                continue

            visited[n] = True
            q.append(n)

    return False

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)

for i in range(n):
    result = []
    for j in range(n):
        num = 1 if bfs(i, j, n) else 0
        result.append(num)
    print(*result)
