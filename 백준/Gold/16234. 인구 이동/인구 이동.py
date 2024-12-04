N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
while True:
    q = []
    visited = [[False] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for i in range(N):
            union = []
            if not visited[j][i]:
                count += 1
                q.append([j, i])
                visited[j][i] = True
                move = 0
                while q:
                    y, x = q.pop()
                    union.append([y, x])
                    move += board[y][x]
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[ny][nx]:
                                if L <= abs(board[y][x] - board[ny][nx]) <= R:
                                    visited[ny][nx] = True
                                    q.append([ny, nx])

                avg = move // len(union)
                for y, x in union:
                    board[y][x] = avg
    if count == N * N:
        break
    else:
        answer += 1


print(answer)