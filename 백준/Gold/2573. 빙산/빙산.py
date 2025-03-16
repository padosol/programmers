from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time = 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in d:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m:
                # 바다 이면
                if graph[nx][ny] == 0:
                    visited[cx][cy] += 1

                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1


while True:
    count = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] > 0:
                bfs(i, j)
                count += 1

    if count >= 2:
        print(time)
        break

    if count == 0:
        print(0)
        break

    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    graph[i][j] = 0

    time += 1