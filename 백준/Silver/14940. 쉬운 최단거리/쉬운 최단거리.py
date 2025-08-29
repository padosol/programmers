from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


find_start = False
start = []
for i in range(n):
    if find_start:
        break
    for j in range(m):
        if arr[i][j] == 2:
            start = [i, j]
            find_start = True
            break


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    result = [[0] * (m) for _ in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    result[nx][ny] = result[x][y] + 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                result[i][j] = -1

        print(*result[i])  


bfs(start[0], start[1])
