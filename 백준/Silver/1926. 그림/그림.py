from collections import deque
n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(ii, jj):
    q = deque()
    q.append([ii, jj])
    count = 0
    while q:
        x, y = q.pop()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return count

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
count = 0
answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            count += 1
            result = bfs(i, j)
            answer = max(answer, result)

print(count)
print(answer)

