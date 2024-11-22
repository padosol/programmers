from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 한칸씩
def dfs(y, x, cnt, idx):
    global answer
    if idx == 4:
        answer = max(answer, cnt)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, cnt + board[ny][nx], idx + 1)
            visited[ny][nx] = False


def bfs(y, x, idx):
    global answer
    for i in range(4):
        q = deque()
        for j in range(4):
            # 방향 하나 차단
            if i == j:
                continue

            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= nx < M and 0 <= ny < N:
                q.append((ny, nx))

        count = 0
        if len(q) == 3:
            count += idx
            a = q.pop()
            count += board[a[0]][a[1]]
            b = q.pop()
            count += board[b[0]][b[1]]
            c = q.pop()
            count += board[c[0]][c[1]]

            answer = max(answer, count)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

answer = 0

for j in range(N):
    for i in range(M):
        visited[j][i] = True
        dfs(j, i, board[j][i], 1)
        visited[j][i] = False
        bfs(j, i, board[j][i])

print(answer)
