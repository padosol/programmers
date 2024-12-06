N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1,  0, 0]
dy = [0,  0, -1, 1]

q = []
answer = 0
visited = [[False] * N for _ in range(N)]
for j in range(N):
    for i in range(N):
        if board[j][i] == 9:
            q.append([[j, i, 0]])
            visited[j][i] = True
            board[j][i] = 0
            break

level = 2
exp = 0
answer = 0
while q:
    move_list = q.pop()

    next_move_list = []
    for y, x, time in move_list:

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] <= level and not visited[ny][nx]:
                    visited[ny][nx] = True
                    next_move_list.append([ny, nx, time+1])

    sorted_move_list = sorted(next_move_list, key=lambda x : (x[0], x[1]))

    for y,x,t in sorted_move_list:
        if 0 < board[y][x] <= level - 1:
            board[y][x] = 0
            exp += 1
            answer = t
            next_move_list = [[y,x,t]]
            if exp == level:
                exp = 0
                level += 1

            visited = [[False] * N for _ in range(N)]
            visited[y][x] = True
            break

    if next_move_list:
        q.append(next_move_list)

print(answer)