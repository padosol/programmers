R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]
next_dust = [[0 for _ in range(C)] for _ in range(R)]

machine = []
for j in range(R):
    if board[j][0] == -1:
        machine.append([j,   0])
        machine.append([j+1, 0])
        break


# 위, 우, 아래, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def diffusion():
    for j in range(R):
        for i in range(C):
            if board[j][i] > 0:
                dust = board[j][i] // 5

                for d in range(4):
                    ny = j + dy[d]
                    nx = i + dx[d]

                    if 0 <= nx < C and 0 <= ny < R:
                        if [ny, nx] not in machine:
                            board[j][i] -= dust
                            next_dust[ny][nx] += dust
    for j in range(R):
        for i in range(C):
            if next_dust[j][i] != 0:
                board[j][i] += next_dust[j][i]
                next_dust[j][i] = 0

def machine_up_on():
    # 위
    my, mx = machine[0]
    d = 0
    while True:
        ny = my + dy[d]
        nx = mx + dx[d]

        if 0 <= ny <= machine[0][0] and 0 <= nx < C:
            if board[ny][nx] > 0:
                if board[my][mx] != -1:
                    board[my][mx] = board[ny][nx]
                board[ny][nx] = 0
            my, mx = ny, nx
        else:
            d += 1
            if d == 4:
                break

def machine_on_down():
    my, mx = machine[1]
    d = 0
    while True:
        ny = my + dy[4 - abs(2 + d)]
        nx = mx + dx[4 - abs(2 + d)]

        if machine[0][0] < ny < R and 0 <= nx < C:
            if board[ny][nx] > 0:
                if board[my][mx] != -1:
                    board[my][mx] = board[ny][nx]
                board[ny][nx] = 0
            my, mx = ny, nx
        else:
            d += 1
            if d == 4:
                break


for _ in range(T):
    diffusion()
    machine_up_on()
    machine_on_down()


answer = 0
for j in range(R):
    for i in range(C):
        if board[j][i] > 0:
            answer += board[j][i]

print(answer)

